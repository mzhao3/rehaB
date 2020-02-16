import os

from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__) #create instance of class flask

app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/words", methods = ['POST'])
def words():
    guess = request.form['guess']

    hi = guess.split(',')
    print(hi)
    return render_template("bank.html", content=hi)

if __name__ == "__main__":
    app.debug = True
    app.run()
