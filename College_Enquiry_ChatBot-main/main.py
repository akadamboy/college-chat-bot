from flask import Flask, render_template, request
import json
import random
import json
from intents import intents
import re
app = Flask(__name__)
with open("intents1.json") as file:
    DATA2 = json.load(file)
DATA2 = DATA2['intents']
DATA = sorted(intents, key=lambda x: len(x))

print(DATA)


def getFaculty():
    return '<img src="./static/pic.png" width="500px" height="300px">'

def getMCAFaculty():
    return 'MCA faculty'


FUNCTIONS = {("faculty", "mca"): getMCAFaculty,
("faculty",): getFaculty}


def getresponse(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    for keyTuple in FUNCTIONS: #mca faculty
        flag = False #("faculty", "")
        for key in keyTuple: #faculty
            if key not in text:
                flag = True
                break
        if flag:
            continue
        return FUNCTIONS[keyTuple]()
    for each in DATA:

        print(each.keys())
        words = text.split()
        flag = False
        for keyTuple in each.keys():
            for key in keyTuple:
                print(key)
                if key not in words:
                    flag = True
                    break
            if flag:
                continue
            return random.choice(each[keyTuple])
    return "Sorry, I didnt understandt that. would you like to chat with a human instead?"


def chat(inp):
    while True:
        response = getresponse(inp)
        return response


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chat(userText))


if __name__ == "__main__":
    app.run()
    # while True:
    #     text = input("Enter a message: ")
    #     print(getresponse(text))
