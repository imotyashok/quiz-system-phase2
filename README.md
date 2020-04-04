# Online Quizzing System

## Project Overview 
This is an online application which allows users to make and take quizzes. Students and professors will be able to log in so that they could save the quizzes they make or to save the results from the quizzes they took. 

## Running the project
In order to view the project at this stage, you must clone this repository, navigate to the directory where the project is located on your machine, and run it in terminal. 

#### Windows
To run on Windows, you'll need to open command prompt (type 'cmd' into the search bar and hit enter), cd into the project directory, and simply type ```run```. After running the command, you will be able to access the site through your localhost domain in your web browser (enter ```http://127.0.0.1:5000/``` in the url bar).   

#### Linux/MAC OS
To run on Linux or Mac machines, cd into the project directory in terminal and enter the following command: ```./run.sh ``` . After running the command, you will be able to access the site through your localhost domain in your web browser (enter ```http://127.0.0.1:5000/``` in the url bar). 

*NOTE:* If you're having problems getting it to run on Linux, make sure you run the following commands to allow the run.sh and init.sh files to be executable: ``` chmod +x run.sh init.sh ```

## Development Notes
1. This project uses Flask and Python, so in order to work on the development of it, you need to have the following requirements met:
- Make sure you have Python 3 and an IDE to work in (the installation comes with IDLE, but if you want something a little more advanced I recommend PyCharm)
- You'll need to get Flask; to do this, simply run the command ```pip install Flask``` in terminal

2. When you're working on the HTML files, you'll need to include the following for each HTML page you make:
```
{% extends "layout.html" %}
{% block content %}

    [ your regular html here ] 

{% endblock content %}
```
This is Jinja2, a templating language for python. The first line connects directly with the layout.html file, from which each page will inherit the layout and styling. The {% block content %} stuff attaches directly to the body of the layout.html file. 
