from flask_wtf import FlaskForm
from wtforms import *

class QuestionTypesForm(FlaskForm):
    # Asks users how many questions of each type they want on the quiz they're making
    # TO-DO: Implement field validators 
    
    multiple_choice = IntegerField("Multiple Choice:")
    
    true_false = IntegerField("True False:")
    
    fill_in_blank = IntegerField("Fill in the Blank:")
    
    submit = SubmitField("Submit")
    
class MultipleChoiceForm(FlaskForm):
    # Form that allows user to create their custom multiple choice question 
    # TO-DO (maybe): allow user to dynamically select how many choices they want rather than hard-code 4 choices 

    question = StringField("Enter your question here:")
    c1 = StringField("Option A:")
    c2 = StringField("Option B:")
    c3 = StringField("Option C:")
    c4 = StringField("Option D:")
    answer = SelectField('Correct answer:', choices=[("a", "A"),("b","B"),("c","C"),("d","D")]) 
   # ... figure out how to make a dropdown for this part 
    # answer = StringField("Correct answer:")

class TrueFalseForm(FlaskForm):
    # TO-DO: implement creation of true false questions 
    question = StringField("Enter your question here:")
    answer = SelectField("Correct answer:", choices=[("t","True"), ("f","False")])

class FillInBlankForm(FlaskForm):
    # TO-DO: implement creation of matching questions 
    question = StringField("Enter your question here:")
    answer = StringField("Enter the correct answer:")

class QuizBuilderForm(FlaskForm):
    # Puts all the question types forms together

    mc = FormField(MultipleChoiceForm)
    tf = FormField(TrueFalseForm)
    fib = FormField(FillInBlankForm) 

    submit = SubmitField("Save Quiz")

