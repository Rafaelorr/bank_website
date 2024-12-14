from sqlite3 import Cursor, Connection, connect

con :Connection = connect("database.db")
cur :Cursor = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS accounts(naam TEXT PRIMARY KEY, wachtwoord TEXT, balance INTEGER)")
con.commit()