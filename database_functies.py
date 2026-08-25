from sqlite3 import Cursor, Connection, connect
from custom_errors import AccountNotFound, NotEnoughFunds

def sign_up_account(naam:str, wachtwoord:str, begin_cash:int):
    """
    De database logica voor het sign up systeem.
    Opzettelijk kwetsbaar voor sql injections.
    """

    # Maak connectie met de database
    con :Connection = connect("database.db")
    cur :Cursor = con.cursor()

    # voeg een nieuw account (met naam, wachtwoord, begin_balance) toe aan de database
    cur.execute(f"INSERT INTO accounts('naam', 'wachtwoord', 'balance') VALUES({naam},{wachtwoord},{begin_cash})")

    # Stop connectie met de database
    con.commit()
    cur.close()
    con.close()

def delete_account(naam:str, wachtwoord:str):
    """
    De database logica om een account te verwijderen.
    Opzettelijk kwetsbaar voor sql injections.
    """
    # Maak connectie met de database
    con : Connection = connect("database.db")
    cur :Cursor = con.cursor()

    # verwijder de account met de ingegeven naaam
    cur.execute(f"DELETE from accounts where naam='{naam}' AND wachtwoord='{wachtwoord}'")

    # Stop connectie met de database
    con.commit()
    cur.close()
    con.close()

def login_account(naam: str, wachtwoord: str) -> tuple[str, str]:
    """
    De database logica voor het login systeem.
    Opzettelijk kwetsbaar voor sql injections.
    """

    # Maak connectie met de database
    con: Connection = connect("database.db")
    cur: Cursor = con.cursor()

    # check of een account met de ingegeven naam en wachtwoord bestaat
    cur.execute(f"SELECT naam, wachtwoord FROM accounts WHERE naam='{naam}' AND wachtwoord='{wachtwoord}'")
    row = cur.fetchone()

    # Stop connectie met de database
    cur.close()
    con.close()

    if row is None:
        raise ValueError("No matching account found.")

    return row


def transaction_system(ontvanger:str, verzender:str, bedrag:int):
    """
    De database logica voor transacties tussen gebruiksers.
    Opzettelijk kwetsbaar gemaakt voor sql injections.
    """

    # Maak connectie met de database
    con :Connection = connect("database.db")
    cur :Cursor = con.cursor()

    # Check of de ontvanger bestaat
    res = cur.execute(f"SELECT naam FROM accounts WHERE naam = '{ontvanger}'")
    if res.fetchone() is None:
        raise AccountNotFound()

    # Check of het account genoeg geld heeft
    res = cur.execute(f"SELECT * FROM accounts WHERE balance >= {bedrag} AND naam = '{verzender}'")
    if res.fetchone() is None:
        raise NotEnoughFunds()

    # Voeg het bedrag toe aan het account van de ontvanger
    cur.execute(f"UPDATE accounts SET balance = balance + {bedrag} WHERE naam = '{ontvanger}'")

    # Trek het bedrag af van het account van de zender
    cur.execute(f"UPDATE accounts SET balance = balance - {bedrag} WHERE naam = '{verzender}'")

    # Stop connectie met de database
    con.commit()
    cur.close()
    con.close()
