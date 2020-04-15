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
    # This function gets and returns the results of the QuestionTypesForm, which asks users 
    # how many questions they want of each question type (multiple choice, true false, and matching)

    form = QuestionTypesForm() # we create our form object 
    if form.is_submitted():
        # Get the results of the form; these are stored as a dictionary, with the key
        # being the variable name of each field on our form (ex. for this one, the keys
        # would be 'multiple_choice', 'true_false', 'matching', and 'submit') and the 
        # values being the actual values the user inputs for those fields 
        result = request.form

        # Now we pass the dictionary of form questions/answers to the createquiz page
        return createquiz(result)    

    return render_template('questiontypes.html', title='Begin Building Your Quiz', form=form)

@app.route("/createquiz", methods=['GET', 'POST']) 
def createquiz(result):
    # Now we can use the dictionary of how many questions of each type the person wants in order to 
    # generate the form that actually lets them build the quiz 

    # Getting the number of each question that the user wanted  
    mc_num = int(result['multiple_choice'])
    tf_num = int(result['true_false'])
    fib_num = int(result['fill_in_blank'])

    form = QuizBuilderForm()
        # TO-DO: figure out what needs to be done once the final form gets submitted  
        # if form.is_submitted():
        #    do stuff... 

    # NOTE: form.mc accesses the MultipleChoiceForm, form.tf accesses the TrueFalseForm, and 
    #       form.match accesses MatchingForm; to access individual fields from each form in your HTML, just 
    #       add another method call;
    #           ex. To access the "question" field of the MultipleChoiceForm, you'd do 'form.mc.question' 

    return render_template('createquiz.html', title='Create Quiz Results', form=form, 
                            mc_num=mc_num, tf_num=tf_num, fib_num=fib_num)
    
    
    