# This file initializes our actual Flask application 

from flask import Flask
from flask_socketio import SocketIO

# creating our app
app = Flask(__name__, static_url_path="/static")

# assigning secret key in order to encrypt our cookies and safely send them to the browser
app.config['SECRET_KEY'] = '77a2c153f819019e8657ceea0848de0d'
app.config["QUIZ_FILE"] = "C:/Users/iryna/quiz-system-phase2/quiz_app/static"

# creating socketio instance
socketio = SocketIO(app)

# importing our routes.py and forms.py files
from quiz_app import routes
from quiz_app import forms
