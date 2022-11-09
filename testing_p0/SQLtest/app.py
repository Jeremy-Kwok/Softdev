import sqlite3

DB_FILE="tables.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

username = "boss"
username1 = "help"
password = "1234"

#Register
c.execute("create table if not exists accounts(username text, password text);") #creates a table called accounts if it doesn't exist
c.execute("insert into accounts values('boss','1234');")
c.execute("select * from accounts")

db.commit() #save changes
db.close()  #close database

DB_FILE="tables.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#Login
login_statement = f"SELECT username from accounts WHERE username='{username1}' AND Password = '{password}';"
username_check = f"select username from accounts where username='{username}';"
c.execute(login_statement)
if c.fetchone():  # An empty result evaluates to False.
    print("Welcome")
else:
    c.execute(username_check)
    if c.fetchone():
        print("Password failed")
    else: 
        print("username not found")