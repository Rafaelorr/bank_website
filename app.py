from sqlite3 import IntegrityError
from random import choice
import string
from flask import Flask, render_template, request, session, redirect, url_for, flash
from custom_errors import AccountNotFound, NotEnoughFunds
from database_functies import sign_up_account, delete_account, login_account, transaction_system


def get_random_character() -> str:
    """Deze functie geeft een random letter, cijfer of symbool terug."""
    return choice(string.ascii_letters + string.digits + string.punctuation)

app = Flask(__name__)
app.config["SECRET_KEY"] = ''.join(get_random_character() for _ in range(50))

@app.route("/")
def home():
    """De start pagina."""
    return render_template("home.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    """De backend logica voor het sign up systeem."""
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
    """De backend logica om je account te kunnen verwijderen."""
    if request.method == "POST":
        naam :str = request.form.get("naam")
        wachtwoord :str = request.form.get("wachtwoord")

        if naam == session.get("naam") and wachtwoord == session.get("wachtwoord"):
            session.clear()
            delete_account(naam,wachtwoord)

            flash(f"{naam}'s account is succesvol gedelete.","succes")

            return render_template("succes.html")
        if session.get("naam") is None or session.get("wachtwoord") is None:
            flash("Je moet ingeloged zijn om je account te deleten.","error")

            return redirect(url_for("login"))
        if session.get("naam") != naam or session.get("wachtwoord") != wachtwoord:
            flash("Foute gegevens","error")

            return redirect(url_for("login"))
    return render_template("delete.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """De backend logica voor het login systeem."""
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

        session.clear()
        flash("Deze gegevens zijn niet correct.","error")

        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/transaction",methods=["GET","POST"])
def transaction():
    """De backend logica voor de transactie pagina."""
    if request.method == "POST":
        ontvanger = request.form.get("ontvanger")
        bedrag = request.form.get("hoeveelheid")

        if session.get("naam") and session.get("wachtwoord"):

            try:
                transaction_system(ontvanger,session.get("naam"),bedrag)
                flash(f"Je transactie naar {ontvanger} is succesvol verlopen.","succes")

                return render_template("succes.html")
            except AccountNotFound:
                flash("Account van je verzender is niet gevonden.","error")

                return redirect(url_for("transaction"))
            except NotEnoughFunds:
                flash("Je hebt niet genoeg geld.","error")

                return redirect(url_for("transaction"))
        else:
            flash("Je moet ingelogde zijn om een transactie te maken.","error")

            return redirect(url_for("transaction"))
    return render_template("transaction.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
