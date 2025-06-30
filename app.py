from flask import Flask, render_template, request, session, redirect, url_for, flash, get_flashed_messages
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
          flash(f"{naam}'s account is succesvol aangemaakt.","succes")
          return render_template("succes.html")
        except IntegrityError:
          flash(f"{naam} is al in gebruik.","error")
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
            flash(f"{naam}'s account is succesvol gedelete.","succes")
            return render_template("succes.html")
        elif session.get("naam") == None or session.get("wachtwoord") == None:
            flash(f"Je moet ingeloged zijn om je account te deleten.","error")
            return redirect(url_for("login"))
        elif session.get("naam") != naam or session.get("wachtwoord") != wachtwoord:
            flash(f"Foute gegevens","error")
            return redirect(url_for("login"))
    return render_template("delete.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        naam = request.form.get("naam")
        wachtwoord = request.form.get("wachtwoord")

        try:
            database_naam, database_wachtwoord = login_account(naam, wachtwoord)
        except ValueError:
            flash("Account bestaat niet.","error")
            return redirect(url_for("login"))

        if naam == database_naam and wachtwoord == database_wachtwoord:
            session["naam"] = naam
            session["wachtwoord"] = wachtwoord
            return redirect(url_for("transaction"))
        else:
            session.clear()
            flash("Deze gegevens zijn niet correct.","error")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/transaction",methods=["GET","POST"])
def transaction():
    if request.method == "POST":
        ontvanger = request.form.get("ontvanger")
        bedrag = request.form.get("hoeveelheid")
        if session.get("naam") and session.get("wachtwoord"):
            try:
              transaction_system(ontvanger,session.get("naam"),bedrag)
              flash(f"Je transactie naar {ontvanger} is succesvol verlopen.","succes")
              return render_template("succes.html")
            except account_not_found:
                flash("Account van je verzender is niet gevonden.","error")
                return redirect(url_for("transaction"))
            except not_enough_funds:
                flash(f"Je hebt niet genoeg geld.","error")
                return redirect(url_for("transaction"))
        else:
            # template met bericht 
            flash("Je moet ingelogde zijn om een transactie te maken.","error")
            return redirect(url_for("transaction"))
    return render_template("transaction.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")