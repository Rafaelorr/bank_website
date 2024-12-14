from sqlite3 import Cursor, Connection, connect

def basic_connection(database_naam:str):
    con :Connection = connect(database_naam)
    cur :Cursor = con.cursor()
    return con, cur

def sign_up_account(naam:str, wachtwoord:str, begin_cash:int):
  con :Connection = connect("database.db")
  cur :Cursor = con.cursor()  

  cur.execute("INSERT INTO accounts('naam', 'wachtwoord', 'balance') VALUES(?,?,?)", (naam, wachtwoord, begin_cash))

  con.commit()
  cur.close()
  con.close()


def delete_account(naam:str, wachtwoord:str):
    pass

def login_account(naam:str, wachtwoord:str):
    pass

def transaction_account(ontvanger:str, hoeveelheid:int):
    pass

def sla_verandering_op(con: Connection,cur: Cursor):
    con.commit()
    cur.close()
    con.close()