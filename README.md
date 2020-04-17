# Online Quizzing System

## Project Overview 
This is an online application which allows users to make and take quizzes. Students and professors will be able to log in so that they could save the quizzes they make or to save the results from the quizzes they took. 

## Running the project
In order to view the project at this stage, you must clone this repository, navigate to the directory where the project is located on your machine, and run it in terminal. 

To run it, simply type ```python run.py``` in the project directory. 

After running the command, you will be able to access the site through your localhost domain in your web browser (enter ```http://127.0.0.1:5000/``` in the url bar).

_NOTE:_ depending on how you installed Python on your machine, you might have to type ```python3 run.py``` or something similar to get the program to run.   

## Development Notes
1. This project uses Flask and Python, so in order to work on the development of it, you need to have the following requirements met:
    - Make sure you have Python 3 and an IDE to work in (the installation comes with IDLE, but if you want something a little more advanced I recommend PyCharm)
    - You'll need to get Flask; to do this, simply run the command ```pip install Flask``` in terminal

2. Whenever you're making a new page for the website, you have to add that page into the "routes.py" file by creating a new route for it:
    ```
    @app.route("/home")
    def home():
        return render_template('home.html', title='Home Page')
    ```
    This adds a route for a homepage on the web app, and it's displayed using the home.html file. 

3. When you're working on the HTML files, you'll need to include the following for each HTML page you make:
    ```
    {% extends "layout.html" %}
    {% block content %}

        [ your regular html here ] 

    {% endblock content %}
    ```
    This is Jinja2, a templating language for python. The first line connects directly with the layout.html file, from which each page   will inherit the layout and styling. The _{% block content %}_ stuff attaches directly to the body of the layout.html file. 
