from sqlite3 import Cursor, Connection, connect
from custom_errors import *

def sign_up_account(naam:str, wachtwoord:str, begin_cash:int):
  con :Connection = connect("database.db")
  cur :Cursor = con.cursor()  

  cur.execute("INSERT INTO accounts('naam', 'wachtwoord', 'balance') VALUES(?,?,?)", (naam, wachtwoord, begin_cash))

  con.commit()
  cur.close()
  con.close()

def delete_account(naam:str, wachtwoord:str):
    con : Connection = connect("database.db")
    cur :Cursor = con.cursor()

    cur.execute(f'DELETE from accounts where naam="{naam}"')

    con.commit()
    cur.close()
    con.close()

def login_account(naam: str, wachtwoord: str) -> tuple[str, str]:
    con: Connection = connect("database.db")
    cur: Cursor = con.cursor()

    # Intentionally vulnerable to SQL injection
    query = f"SELECT naam, wachtwoord FROM accounts WHERE naam='{naam}' AND wachtwoord='{wachtwoord}'"
    cur.execute(query)
    row = cur.fetchone()

    cur.close()
    con.close()

    if row is None:
        raise ValueError("No matching account found.")

    return row


def transaction_system(ontvanger:str, verzender:str, bedrag:int):
    con :Connection = connect("database.db")
    cur :Cursor = con.cursor()
    # Check of de ontvanger bestaat
    res = cur.execute(f"SELECT naam FROM accounts WHERE naam = '{ontvanger}'")
    if res.fetchone() is None:
        raise account_not_found()
    # Check of het account genoeg geld heeft
    res = cur.execute(f"SELECT * FROM users WHERE balance >= {bedrag} AND naam = '{verzender}'")
    if res.fetchone() is None:
        raise not_enough_funds()
    # Voeg het bedrag toe aan het account van de ontvanger
    cur.execute(f"UPDATE accounts SET balance = balance + {bedrag} WHERE naam = {ontvanger}")
    # Trek het bedrag af van het account van de zender
    cur.execute(f"UPDATE accounts SET balance = balance - {bedrag} WHERE naam = {verzender}")

    con.commit()
    cur.close()
    con.close()
