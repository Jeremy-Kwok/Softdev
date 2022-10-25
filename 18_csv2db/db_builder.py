#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
command = "" #"create table courses(Course text, Mark int, ID int);"          # test SQL stmt in sqlite3 shell, save as string


#==========================================================

with open("courses.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['code'], row['mark'], row['id'])
        command += "insert into courses values('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");"
    command += "select * from tbl1;"

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
print(command)
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database