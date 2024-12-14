from flask import Flask, render_template, request
from sqlite3 import IntegrityError
from database_functies import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        naam = request.form.get("naam")
        wachtwoord = request.form.get("wachtwoord")
        begin_cash = request.form.get("begin_cash")
        print(naam)
        print(wachtwoord)
        print(begin_cash)
        try:
          sign_up_account(naam,wachtwoord,begin_cash)
          return render_template("succes.html")
        except IntegrityError:
          return render_template("fail.html")
    return render_template("sign_up.html")

@app.route("/delete",methods=["GET","POST"])
def delete():
    if request.method == "POST":
        naam = request.form.get("naam")
        wachtwoord = request.form.get("wachtwoord")
    return render_template("delete.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        naam = request.form.get("naam")
        wachtwoord = request.form.get("wachtwoord")
    return render_template("login.html")

@app.route("/transaction",methods=["GET","POST"])
def transaction():
    if request.method == "POST":
        ontvanger = request.form.get("ontvanger")
        hoeveelheid = request.form.get("hoeveelheid")
    return render_template("transaction.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")