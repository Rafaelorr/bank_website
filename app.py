from flask import Flask, render_template, request, session, redirect, url_for
from sqlite3 import IntegrityError
from database_functies import *
from random import choice
import string

alphabet = string.ascii_letters + string.digits + string.punctuation

app = Flask(__name__)
app.config["SECRET_KEY"] = ''.join(choice(alphabet) for _ in range(40))

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
          bericht = f"{naam}'s account is succesvol aangemaakt."
          return render_template("succes.html", resulaat=bericht)
        except IntegrityError:
          bericht = f"{naam} is al in gebruik."
          return render_template("fail.html", resulaat=bericht)
    return render_template("sign_up.html")

@app.route("/delete",methods=["GET","POST"])
def delete():
    if request.method == "POST":
        naam :str = request.form.get("naam")
        wachtwoord :str = request.form.get("wachtwoord")
        if naam == session.get("naam") and wachtwoord == session.get("wachtwoord"):
            session.clear()
            delete_account(naam,wachtwoord)
            bericht = f"{naam}'s account is succesvol gedelete."
            return render_template("succes.html", resulaat=bericht)
        elif session.get("naam") == None and session.get("wachtwoord") == None:
            return redirect(url_for("login"))
    return render_template("delete.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        naam = request.form.get("naam")
        wachtwoord = request.form.get("wachtwoord")

        database_naam, database_wachtwoord = login_account(naam,wachtwoord)

        if naam == database_naam and wachtwoord == database_wachtwoord:
            session["naam"] = naam
            session["wachtwoord"] = wachtwoord
            return redirect(url_for("transaction"))
        else:
            session.clear()
            bericht = f"Deze gegevens zijn niet correct."
            return render_template("login.html",resulaat=bericht)
    return render_template("login.html",resulaat="")

@app.route("/transaction",methods=["GET","POST"])
def transaction():
    if request.method == "POST":
        ontvanger = request.form.get("ontvanger")
        hoeveelheid = request.form.get("hoeveelheid")
    return render_template("transaction.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")