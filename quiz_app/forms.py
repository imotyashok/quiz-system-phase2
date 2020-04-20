from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class QuestionTypesForm(FlaskForm):
    # Asks users how many questions of each type they want on the quiz they're making
    # TO-DO: Implement field validators 

    multiple_choice = IntegerField("Multiple Choice:", validators=[DataRequired()])

    true_false = IntegerField("True False:", validators=[DataRequired()])

    fill_in_blank = IntegerField("Fill in the Blank:", validators=[DataRequired()])

    submit = SubmitField("Submit")


class MultipleChoiceForm(FlaskForm):
    # Form that allows user to create their custom multiple choice question 
    # TO-DO (maybe): allow user to dynamically select how many choices they want rather than hard-code 4 choices 

    question = StringField("Enter your question here:", validators=[DataRequired()])
    c1 = StringField("Option A:", validators=[DataRequired()])
    c2 = StringField("Option B:", validators=[DataRequired()])
    c3 = StringField("Option C:", validators=[DataRequired()])
    c4 = StringField("Option D:", validators=[DataRequired()])
    answer = SelectField('Correct answer:', choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")])
    # ... figure out how to make a dropdown for this part
    # answer = StringField("Correct answer:")


class TrueFalseForm(FlaskForm):
    # TO-DO: implement creation of true false questions 
    question = StringField("Enter your question here:", validators=[DataRequired()])
    answer = SelectField("Correct answer:", choices=[("t", "True"), ("f", "False")])


class FillInBlankForm(FlaskForm):
    # TO-DO: implement creation of matching questions 
    question = StringField("Enter your question here:", validators=[DataRequired()])
    answer = StringField("Enter the correct answer:", validators=[DataRequired()])


class QuizBuilderForm(FlaskForm):
    # Puts all the question types forms together

    mc = FormField(MultipleChoiceForm)
    tf = FormField(TrueFalseForm)
    fib = FormField(FillInBlankForm)

    submit = SubmitField("Save Quiz")

