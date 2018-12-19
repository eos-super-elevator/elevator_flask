from flask import Flask, Response
from components.LCD.I2CLCD1602 import display


app = Flask(__name__)

@app.route("/")
def hello():
    content = """<h1>Elevator web server</h1>
    <p>An Python Flask web server to master some Raspberry PI components. This server expose some routes:</p>

    <ul> 
      <li>GET `/lcd/display/<content>`</li>
      <li>GET `/led/blink`</li>
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
