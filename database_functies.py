from sqlite3 import Cursor, Connection, connect

def basic_connection(database_naam:str):
    con = connect(database_naam)
    cur = con.cursor()
    return con, cur

def sign_up_account(naam:str, wachtwoord:str, begin_cash:int):
    pass

def delete_account(naam:str, wachtwoord:str):
    pass

def login_account(naam:str, wachtwoord:str):
    pass

def transaction_account(ontvanger:str, hoeveelheid:int):
    pass