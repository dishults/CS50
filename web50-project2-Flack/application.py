import os, time

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

messages = {} #channel : [{message, user, time}]

@app.route("/")
def index():
    if 'username' in session:
        return render_template("last_page.html")
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form.get('username')
    return redirect(url_for('channels'))

@app.route("/channels")
def channels():
    return render_template("channels.html", channels=messages)

@app.route("/channels/<string:name>")
def channel(name):
    # if channel doesn't exist redirect to channels creation page
    if name not in messages:
        return redirect(url_for('channels'))
    elif len(messages[name]) > 100:
        messages[name] = messages[name][-100:]
    return render_template("channel.html", channel=name, messages=messages[name])

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@socketio.on("add channel")
def chnl(data):
    channel = data["new_channel"]
    messages[channel] = []
    emit("all channels", data, broadcast=True)

@socketio.on("send message")
def msg(data):
    channel = data["channel_name"]

    msg = data["message"]
    if msg.startswith('@') > 0:
        if msg.startswith('@time'):
            msg = time.strftime("It's currently %H:%M:%S")
        elif msg.startswith('@date'):
            msg = time.strftime("Today is %Y-%m-%d")
        elif msg.startswith('@len'):
            nb = len(messages[channel])
            msg = f"There are currently {nb} message(s) in *{channel}* channel"
        elif msg.startswith('@me'):
            msg = f"Your username is {session['username']}"
        elif msg.startswith('@channels'):
            str1 = ""
            for c in [ch for ch in messages]:
                str1 += c + " "
            msg = f"Available channels: {str1}"
    
    message = {"message" : msg,
                "user" : session['username'],
                "time" : time.strftime("%Y-%m-%d %H:%M:%S")}


    messages[channel].append(message)

    emit("all messages", message, broadcast=True)