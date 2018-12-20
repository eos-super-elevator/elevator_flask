from flask import Flask, Response
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

from components.LCD.I2CLCD1602 import display
from components.ultrasonic_ranging import loop_during


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
cors = CORS(app,resources={r"/socket.io/*":{"origins":"*"}})
socketio = SocketIO(app)

@app.route("/")
def hello():
    content = """<h1>Elevator web server</h1>
    <p>An Python Flask web server to master some Raspberry PI components. This server expose some routes:</p>

    <ul>
      <li>GET <a href="/lcd/display/helloworld">/lcd/display/<content></a></li>
      <li>GET <a href="/led/blink">/led/blink</a></li>
      <li>GET <a href="/sonar/run">/sonar/run/<int:time></a></li>
    </ul>
    """
    return Response(content, mimetype='text/html')

@app.route('/lcd/display/<content>')
def display_lcd(content):
    """Simply read content from URI & display message on LCD screen
    """
    display(content)
    return content

@app.route('/led/blink')
def blink_led():
    """Make LED blink during 5 seconds
    """
    # TODO
    pass


@app.route('/sonar/run/<int:time>')
def run_sonar(time):
    """Simply read content from URI & display message on LCD screen
    """
    for distance in loop_during(time):
        emit('sonar', (distance), broadcast=True, namespace="/")
    return "finished"


@socketio.on('message')
def handle_message(message):
  print('received message: ' + message)

@socketio.on('message')
def handle_message(message):
  print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
  print('received json: ' + str(json))

if __name__ == '__main__':
  socketio.run(app)
