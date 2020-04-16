from flask import render_template, request, redirect, url_for
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
        # values being the actual number values the user inputs for those fields 
        result = request.form

        # Extracting the values the user submitted in the form 
        mc_num = result['multiple_choice']
        tf_num = result['true_false']
        fib_num = result['fill_in_blank']

        # Now we pass the numbers of question types the user entered to the createquiz page
        return redirect(url_for("createquiz", mc_num=mc_num, tf_num=tf_num, fib_num=fib_num))   
        
    return render_template('questiontypes.html', title='Begin Building Your Quiz', form=form)

@app.route("/createquiz/<mc_num>_<tf_num>_<fib_num>", methods=['GET', 'POST']) 
def createquiz(mc_num, tf_num, fib_num):
    # Now we can use the number of each question type the user wanted in order to 
    # generate the form that actually lets them build the quiz 

    # Converting these numbers to integer type: 
    mc_num, tf_num, fib_num = int(mc_num), int(tf_num), int(fib_num)
    
    form = QuizBuilderForm() # Generating the actual quiz building form 
    # TO-DO: figure out what needs to be done once the final form gets submitted  
    if form.is_submitted():
        #    do stuff...
        result = request.form

        # NOTE: The results are stored in a dictionary that follows this format:
        # print(result) --> 
        # ImmutableMultiDict([('mc-question', 'What color is a banana?'), ('mc-c1', 'Purple'), 
        #                      ('mc-c2', 'Green'), ('mc-c3', 'Yellow'), ('mc-c4', 'Red'), 
        #                      ('mc-answer', 'c'), ('tf-question', 'Computer mice are mammals. '), 
        #                      ('tf-answer', 'f'), ('fib-question', 'The best OS is'), 
        #                      ('fib-answer', 'Linux'), ('submit', 'Save Quiz')])
        #
        # Some problems with questions of the same type... ex:
        # ImmutableMultiDict([('tf-question', 'Computer mice are mammals. '), 
        #                     ('tf-question', 'Python is both a programming language and a snake'), 
        #                     ('tf-question', 'Some flowers are yellow. '), ('tf-answer', 'f'), 
        #                     ('tf-answer', 't'), ('tf-answer', 't'), ('submit', 'Save Quiz')])

        mc_q_list = request.form.getlist('mc-question')
        mc_c1_list = request.form.getlist('mc-c1')
        mc_c2_list = request.form.getlist('mc-c2') 
        mc_c3_list = request.form.getlist('mc-c3') 
        mc_c4_list = request.form.getlist('mc-c4')
        mc_ans_list = request.form.getlist('mc-answer') 

        tf_q_list =  request.form.getlist('tf-question')
        tf_ans_list = request.form.getlist('tf-answer')

        fib_q_list = request.form.getlist('fib-question')
        fib_ans_list = request.form.getlist('fib-answer')

        if mc_q_list:
            for q in range(len(mc_q_list)):
                print("Question %d:" %(q+1))
                print(mc_q_list[q], mc_c1_list[q], mc_c2_list[q], mc_c3_list[q], mc_c4_list[q], mc_ans_list[q])
            print("\n")
        if tf_q_list:
            for q in range(len(tf_q_list)):
                print("Question %d:" %(q+1))
                print(tf_q_list[q], tf_ans_list[q])
            print("\n")
        if fib_q_list:
            for q in range(len(fib_q_list)):
                print("Question %d:" %(q+1))
                print(fib_q_list[q], fib_ans_list[q])
            print("\n")

        return redirect(url_for('home')) # redirect to home for now lol
        
    # NOTE: form.mc accesses the MultipleChoiceForm, form.tf accesses the TrueFalseForm, and 
    #       form.match accesses MatchingForm; to access individual fields from each form in your HTML, just 
    #       add another method call;
    #           ex. To access the "question" field of the MultipleChoiceForm, you'd do 'form.mc.question' 

    return render_template('createquiz.html', title='Create Quiz Results', form=form, 
                            mc_num=mc_num, tf_num=tf_num, fib_num=fib_num)
    
    
    