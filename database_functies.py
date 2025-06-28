from sqlite3 import Cursor, Connection, connect

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


def transaction_account(ontvanger:str, hoeveelheid:int):
    pass
