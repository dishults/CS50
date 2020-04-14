import os

from flask import Flask, session, render_template, request, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    "Register new user"

    # Get user info
    if request.method == 'GET':
        return render_template("register.html")

    # Add user to database
    try:
        username = request.form.get("username")
        password = request.form.get("password")
        assert username and password
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": username, "password": password})
        db.commit()
    except AssertionError:
        return render_template("errors.html", message="Couldn't register new user")
    
    return render_template("success.html", message="User has been created!")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
    try:
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.execute("SELECT * FROM users\
            WHERE username=:username AND password=:password",
            {"username": username, "password": password}).fetchone()
        assert user
        session["user_id"] = user.id
        return render_template("search.html")
    except AssertionError:
        return render_template("errors.html", message="Wrong username/password")

@app.route("/logout")
def logout():
    user = session["user_id"]
    session.pop('user_id', None)
    return render_template("success.html", message=f"{user} have been logged out")

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template("search.html")
    
    try:
        option = request.form.get("inlineRadioOptions")
        search = request.form.get("search")
        assert option and search
        results = db.execute(f"SELECT * FROM books WHERE {option} LIKE :search",
            {"search": '%'+search+'%'}).fetchall()
        if not results:
            return render_template("errors.html", message=f"No matches were found for {option} {search}")
        return render_template("results.html", results=results, option=option)
    except AssertionError:
        return render_template("errors.html", message="Wrong ISBN number/Title/Author")

@app.route("/search/<string:isbn>")
def info(isbn):
    results = db.execute("SELECT * FROM books WHERE isbn=:isbn",
        {"isbn": isbn}).fetchone()
    if not results:
        return render_template("errors.html", message=f"No matches were found for {isbn}")
    reviews = db.execute("SELECT * FROM reviews FULL JOIN users ON (reviews.user_id=users.id) WHERE book_id=:isbn",
        {"isbn": isbn}).fetchall()
    return render_template("book.html", results=results, reviews=reviews)

@app.route("/submit-review", method=['POST'])
def review():
    rating = request.form.get("inlineRadioOptions")
    review = request.form.get("review")
    return render_template("success.html", message=f"User {session['user_id']} gave {rating} stars with an impression: {review}")

#import requests
#res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "i6lzhH6iBz08XjkLn2pv5g", "isbns": "9781632168146"})
#print(res.json()) 