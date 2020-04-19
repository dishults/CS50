import os

from flask import Flask, request, session
from flask_socketio import SocketIO, emit
from flask.templating import render_template
from markupsafe import escape
from werkzeug import redirect
from flask.helpers import url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.secret_key = os.getenv("SECRET_KEY")

all_channels = set()
messages = {"hey": ["what's up", "how are you?", "hi, everyone"]}

@app.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('channels'))
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    session['username'] = username
    return redirect(url_for('channels'))

@app.route("/channels", methods=['GET', 'POST'])
def channels():
    if request.method == 'POST':
        channel = request.form.get('channelname')
        all_channels.add(channel)
    return render_template("channels.html", channels=all_channels)

@app.route("/channels/<string:name>")
def channel(name):
    messages[name] = messages[name][-100:]
    return render_template("channel.html", channel=name, messages=messages[name])

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
