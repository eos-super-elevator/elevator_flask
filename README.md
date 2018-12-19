# Python Elevator Server

A Python Flask web server to master some Raspberry PI components. This server expose some routes:

- GET `/lcd/display/<content>`
- GET `/led/blink`

Also this use [Socket.io][socketio] & [Flask-Socket.io][flask-socketio] to produce realtime stuffs.

## Components used on Raspberry PI

We use [this kit][freenove_kit] to build the complete system. We use only:

- I2C LCD 1602 for display

## Instalation

[Install Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) then:

    $ pipenv instal
    $ pipenv run pip3 flask run

This will start a production server on <http://localhost:5000>


[freenove_kit]: https://www.amazon.fr/Freenove-Raspberry-Processing-Tutorials-Components/dp/B06W54L7B5
[socketio]: https://socket.io/
[flask-socketio]: https://flask-socketio.readthedocs.io/
