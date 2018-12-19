from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
  print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
  print('received json: ' + str(json))
  emit('chat', secrets.token_hex(nbytes=8))

if __name__ == '__main__':
  socketio.run(app)
