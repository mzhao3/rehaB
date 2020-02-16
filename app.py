import os

from flask import Flask, render_template, request, session, redirect, url_for, flash

from util import wordlib

app = Flask(__name__) #create instance of class flask

app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/words", methods = ['POST'])
def words():
    guess = request.form['guess']
    d = wordlib.get_dict()
    hi = guess.split(',')
    print(hi)
    hi = [i.strip() for i in hi if i in d]

    that = ""
    if not hi:
        that = "You're out of luck! None of the words you found are in the dictionary."
        print(that)
    return render_template("bank.html", content=hi, message = that)

@app.route("/display")
def display():
    to_haiku = request.args.get("input")
    if not to_haiku:
        flash("no valid input error")
        return redirect("/")

    thehaiku = wordlib.get_haiku(to_haiku)
    print(thehaiku)
    return render_template("haiku.html", content = thehaiku)

if __name__ == "__main__":
    app.debug = True
    app.run()
