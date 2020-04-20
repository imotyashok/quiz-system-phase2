
import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

fileToDisplay = 'textfile.txt'

@app.route("/")
def fileFrontPage():
    global fileToDisplay
    textFromFile = open(fileToDisplay, 'r+')
    content = textFromFile.read()
    textFromFile.close()
    return render_template('fileform.html', textQ=content)

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    global fileToDisplay
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            fileToDisplay = os.path.join('C:/Users/Alberto/Desktop/flaskTesting/inputB', photo.filename)
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()