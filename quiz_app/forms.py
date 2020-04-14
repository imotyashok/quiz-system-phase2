from flask_wtf import FlaskForm
from wtforms import *

class QuestionTypesForm(FlaskForm):
    # Asks users how many questions of each type they want on the quiz they're making
    # TO-DO: Implement field validators 
    
    multiple_choice = IntegerField("Multiple Choice:")
    
    true_false = IntegerField("True False:")
    
    matching = IntegerField("Matching:")
    
    submit = SubmitField("Submit")
    
class MultipleChoiceForm(FlaskForm):
    # Form that allows user to create their custom multiple choice question 
    # TO-DO (maybe): allow user to dynamically select how many choices they want rather than hard-code 4 choices 

    question = StringField("Enter your question here:")
    c1 = StringField("Enter Choice 1 value:")
    c2 = StringField("Enter Choice 2 value:")
    c3 = StringField("Enter Choice 3 value:")
    c4 = StringField("Enter Choice 2 value:")

class TrueFalseForm(FlaskForm):
    # TO-DO: implement creation of true false questions 
    pass

class MatchingForm(FlaskForm):
    # TO-DO: implement creation of matching questions 
    pass

class QuizBuilderForm(FlaskForm):
    # Puts all the question types forms together

    mc = FormField(MultipleChoiceForm)
    tf = FormField(TrueFalseForm)
    match = FormField(MatchingForm) 

    submit = SubmitField("Save Quiz")

