from flask import render_template, request
from quiz_app import app
from quiz_app.forms import *

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
    # we create our form object 
    form = QuestionTypesForm()
    if form.is_submitted():
        # Get the results of the form; these are stored as a dictionary, with the key
        # being the variable name of each field on our form (ex. for this one, the keys
        # would be 'multiple_choice', 'true_false', 'matching', and 'submit') and the 
        # values being the actual values the user inputs for those fields 
        result = request.form
        return render_template('createquiz.html', title='Create Quiz Results', result=result)
    return render_template('questiontypes.html', title='Begin Building Your Quiz', form=form)
    
    
    
    