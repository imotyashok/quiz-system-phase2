from flask import Flask, render_template, request
from forms import *
app = Flask(__name__)

app.config['SECRET_KEY'] = '77a2c153f819019e8657ceea0848de0d'

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', title='Home Page')

@app.route("/about")
def about():
    return render_template('about.html', title='About Page')
    
@app.route("/makequiz")
def makequiz():
    return render_template('makequiz.html', title='Make a Quiz')
    
@app.route("/takequiz")
def takequiz():
    return render_template('takequiz.html', title='Take a Quiz')
    
@app.route("/questiontypes", methods=['GET', 'POST'])
def questiontypes():
    form = QuestionTypesForm()
    if form.is_submitted():
        result = request.form
        return render_template('createquiz.html', title='Create Quiz Results', result=result)
    return render_template('questiontypes.html', title='Begin Building Your Quiz', form=form)
    
    
    
    