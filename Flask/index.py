from flask import Flask
import random

app = Flask(__name__)

gifs = [
"https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmRlMGRva3pudHlldWM4ZnVpM3YwcGZyOTg3cWI5cGU1d2Q1c3o2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/61lH8qx8A0JiJXh3h5/giphy.gif",
"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWoyOWU1YjNmeTZkaTI2enExOTliaHlpcjc0YWFhbmgzNTM2eW10aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cdlr2QaQ4o4lEtiXkW/giphy.gif",
"https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDZ1M2FsbG5nMm52b2Y0OTV3ZWFuMWhiMnI0M3llNXQ4Yjc4dnU1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4nSl9oAv5IYHy0eVB1/giphy.gif",
"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGUxNWFqdzNzajdqemt1ZHljNmk5a29wdGV5bW1xMW9yamo0OTl5YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/15aGGXfSlat2dP6ohs/giphy.gif",
"https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWRuaGJsMTN5eXZoa2FucjZneWsxYTg1eHVjM2c3czVuaW9rMDc0aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W5YVAfSttCqre/giphy.gif",
"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWplbjF2eGh2Y2xiMjJlNms4NTVtdjA0aTczdDZlbHRodDRudm10aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sU6yN4mPVwP7wiXB9v/giphy.gif",
"https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG1kNjdpbTh2cWo4M3F2aXNidXY2bnptenpmejUzbng0NWhnNzRpcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26hkhKd2Cp5WMWU1O/giphy.gif",
"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2pqNHdhMHU2dXQ3YWloYW10aTVwMDd1dzdwZnNic2phN2pmbDRheSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nKZEvTua5D4o0XD6Ge/giphy.gif"
]


@app.route('/')
def index():
    return "<h1>Enter a number 0-9</h1>"

@app.route("/<guess>")
def guess(guess):
    if int(guess) == 7:
        return "<img src=https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXRsZGZ2cTJlcHp5Nzl1N3R4NzB4YWtxZmRidHdrcWxpa2NwN2owYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.gif>"
    else:
        link = random.choice(gifs)
        return f"<img src={link}>"


if __name__ == "__main__":
    app.run(debug=True)
