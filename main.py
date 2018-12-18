from flask import Flask
from components.LCD.I2CLCD1602 import display
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/led/<content>')
def profile(content):
    display(content)
    return content
