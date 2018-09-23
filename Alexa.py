from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests

app = Flask(__name__)
ask = Ask(app, "/")

words = ["andrew", "ugly", "gremlin"]

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'One day, '+words[0]+' was walking to class but he was an '+ words[1]+ ' '+ words[2]+ '.'
    return question(welcome_message)

@ask.intent("userInput")
def share_feelings():
    feelings_msg = 'I really do not like you'
    return statement(feelings_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I get it, I do not like you either'
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)


#story = "One day, "+words[0]+" was walking to class but he was stopped by an "+ words[1]+ " "+ words[2]+ "."