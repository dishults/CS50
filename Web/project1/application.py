import os, requests

from flask import Flask, session, render_template, request
from flask.helpers import flash
from flask.json import jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug import redirect

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['JSON_SORT_KEYS'] = False
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/search")
    
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    try:            
        username = request.form.get("username")
        password = request.form.get("password")
        assert username and password

        # Register user
        if request.form.get("register"):
            if db.execute("SELECT * FROM users WHERE username=:username",
                {"username": username}).first():
                return render_template("message.html", message="Username already exists, try logging in instead")
            
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                {"username": username, "password": password})
            db.commit()

        # Log user in
        user = db.execute("SELECT * FROM users\
            WHERE username=:username AND password=:password",
            {"username": username, "password": password}).fetchone()
        assert user
        session["user_id"] = user.id
        return redirect("/search")
    except AssertionError:
        return render_template("message.html", message="Wrong username/password")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect("/")

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template("search.html", param="search")
    
    try:
        option = request.form.get("inlineRadioOptions")
        search = request.form.get("search")
        assert option and search
        results = db.execute(f"SELECT * FROM books WHERE {option} LIKE :search",
            {"search": '%'+search+'%'}).fetchall()
        if not results:
            return render_template("message.html", message=f"No matches were found for {option} {search}")
        return render_template("search.html", results=results, option=option)
    except AssertionError:
        return render_template("message.html", message="Wrong ISBN number/Title/Author")

@app.route("/search/<string:isbn>")
def book(isbn):
    results = db.execute("SELECT * FROM books WHERE isbn=:isbn",
        {"isbn": isbn}).fetchone()
    if not results:
        return render_template("message.html", message=f"No matches were found for {isbn}")

    # Get user reviews from database
    reviews = db.execute("SELECT * FROM reviews FULL JOIN users ON (reviews.user_id=users.id) WHERE book_id=:isbn",
        {"isbn": isbn}).fetchall()

    # Get book's average rating and number of ratings from Goodreads API
    goodreads = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "i6lzhH6iBz08XjkLn2pv5g", "isbns": isbn}).json()
    avg_rating = goodreads["books"][0]["average_rating"]
    ratings_count = goodreads["books"][0]["work_ratings_count"]

    return render_template("book.html", results=results, reviews=reviews, avg_rating=avg_rating, ratings_count=ratings_count)

@app.route("/submit-review/<string:isbn>", methods=['POST'])
def review(isbn):
    rating = request.form.get("inlineRadioOptions")
    review = request.form.get("review")

    if db.execute("SELECT * FROM reviews WHERE book_id=:isbn AND user_id=:id",
        {"isbn": isbn, "id": session["user_id"]}).fetchone():
        return render_template("message.html", message="You've already submitted a review for this book before!")
    
    db.execute("INSERT INTO reviews (review, rating, book_id, user_id) VALUES (:review, :rating, :book_id, :user_id)",
                    {"review": review, "rating": rating, "book_id": isbn, "user_id": session["user_id"]})
    db.commit()

    return render_template("message.html", param="success", message="Thanks for submiting a review!")

@app.route("/api/<string:isbn>", methods=['GET'])
def api(isbn):

    if not db.execute("SELECT isbn FROM books WHERE isbn=:isbn",
        {"isbn": isbn}).fetchone():
        return jsonify({"error": "requested ISBN number not found in the database"}), 404
    
    book = db.execute("SELECT title, author, year, COUNT(review), ROUND(AVG(rating),2) FROM books FULL JOIN reviews ON (books.isbn=reviews.book_id) WHERE isbn=:isbn GROUP BY isbn",
        {"isbn": isbn}).fetchone()
    
    return jsonify ({
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "isbn": isbn,
        "review_count": book.count,
        "average_score": book.round       
    })
