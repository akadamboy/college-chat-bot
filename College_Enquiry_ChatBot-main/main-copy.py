from flask import Flask, render_template, request
import json
import random
import json
import re

app = Flask(__name__)


with open("intents1.json") as file:
    DATA = json.load(file)
DATA = DATA['intents']


def getFaculty():
    return '<img src="./static/pic.png" width="500px" height="300px">'


FUNCTIONS = {"faculty": getFaculty}


def getresponse(text):
    for each in DATA:
        for p in each['patterns']:

            # for i in text.split():
            #     if i in FUNCTIONS:
            #         return FUNCTIONS[i]()

            # if any(x in p for x in text.split()):
            #     resp = random.choice(each['responses'])
            #     return resp
            if(p == text):
                resp = random.choice(each['responses'])
                return resp

    return "Sorry, I didnt understandt that. would you like to chat with a human instead?"


def chat(inp):
    while True:
        response = getresponse(inp)
        return response


@app.route("/")
def home():
    return render_template("/home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chat(userText))


if __name__ == "__main__":
    app.run()
    # while True:
    #     text = input("Enter a message: ")
    #     print(getresponse(text))
