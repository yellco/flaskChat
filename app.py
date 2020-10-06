from flask import Flask, render_template, url_for, redirect, session, request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)


with open('./conf/config.json', 'r') as f:
	data = json.loads(f.read())
	key = data['key']

app.config['SECRET_KEY'] = key

socketio = SocketIO(app, cors_allowed_origins='*')

main = "https://chat.yellco.ru"


@socketio.on('message')
def handleMessage(data):
    print("Message: {}".format(data))
    send(data, broadcast=True)

@socketio.on('connect')
def connect():
    emit('enter', 'подключился', namespace='/chat')
    send('Подключился', broadcast=True)

@socketio.on('chat-message')
def message(data):
    send(data, broadcast=True)

@app.route('/chat/username')
def user():
    if 'username' in session:
        return session.get("username")
    else:
        return 'Username not found', 404

@app.route('/chat/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
        if username:
            return 'Username set'
        else:
            return 'No username in the formdata', 404

@app.route('/chat/logout')
def logout():
    session.pop("username", None)
    return "Logout successful"

if __name__ == "__main__":
    socketio.run(app, port="5100")