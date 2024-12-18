from flask import Flask, render_template, request, session, redirect, url_for
from sqlite3 import IntegrityError
from database_functies import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "7978557dsmlg876+47567895457687hsdmfo)çé!(ç)éç(§è!é)§hsmdqfglé§(éééç)é)))&&&&&(èéà!(§-^$ù$;;;;;=ù$^$$*DHESHESH4343SYITYURTRZYEZRTZAERZAEFSD34534534GHDSsqhgDFGRESZHgdqsgqsdggzegd434343585767454jfdqh74678675gezgezS45786djarezr!§é§$^$HRHSDHRDEH!azeghmsidfgeqszfSQ"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        naam :str = request.form.get("naam")
        wachtwoord :str = request.form.get("wachtwoord")
        begin_cash :int = request.form.get("begin_cash")
        try:
          sign_up_account(naam,wachtwoord,begin_cash)
          session["naam"] = naam
          session["wachtwoord"] = wachtwoord
          return render_template("succes.html")
        except IntegrityError:
          return render_template("fail.html")
    return render_template("sign_up.html")

@app.route("/delete",methods=["GET","POST"])
def delete():
    if request.method == "POST":
        naam :str = request.form.get("naam")
        wachtwoord :str = request.form.get("wachtwoord")
        if naam == session.get("naam") and wachtwoord == session.get("wachtwoord"):
            session.clear()
            delete_account(naam,wachtwoord)
            return render_template("succes.html")
        elif session.get("naam") == None and session.get("wachtwoord") == None:
            return redirect(url_for("login"))
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