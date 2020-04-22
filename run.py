from quiz_app import app
from quiz_app import socketio

if __name__ == '__main__':
    socketio.run(app, debug=True)
