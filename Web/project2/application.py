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
messages = {}

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

@app.route("/channels")
def channels():
    return render_template("channels.html", channels=all_channels)

@app.route("/channels/<string:name>")
def channel(name):
    # If channel has messages
    if name in messages:
        messages[name] = messages[name][-100:]
        return render_template("channel.html", channel=name, messages=messages[name])
    return render_template("channel.html", channel=name)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@socketio.on("add channel")
def chnl(data):
    channel = data["new_channel"]
    all_channels.add(channel)
    emit("all channels", data, broadcast=True)

@socketio.on("send message")
def msg(data):
    channel = data["channel_name"]
    msgs = data["message"]

    if channel not in messages:
        messages[channel] = [(msgs)]
    else:
        messages[channel].append(msgs)

    emit("all messages", data, broadcast=True)