from flask_wtf import FlaskForm
from wtforms import *

class QuestionTypesForm(FlaskForm):
    # Asks users how many questions of each type they want on the quiz they're making
    # TO-DO: Implement field validators 
    
    multiple_choice = IntegerField("Multiple Choice:")
    
    true_false = IntegerField("True False:")
    
    matching = IntegerField("Matching:")
    
    submit = SubmitField("Submit")
    