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

def login_account(naam:str, wachtwoord:str) -> str:
    con :Connection = connect("database.db")
    cur :Cursor = con.cursor()

    cur.execute(f"SELECT * FROM accounts WHERE naam='{naam}' AND wachtwoord='{wachtwoord}'")
    row = cur.fetchone()
    row = tuple(row)

    database_naam = row[0]
    database_wachtwoord = row[1]

    con.commit()
    cur.close()
    con.close()

    return database_naam, database_wachtwoord

def transaction_account(ontvanger:str, hoeveelheid:int):
    pass
