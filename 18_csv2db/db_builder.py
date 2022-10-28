# Team Jelly Jam Pancakes: Jacob, Jeremy, Prattay
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022
#Time Spent: 1.0

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="tables.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#c.execute(".mode markdown")
#c.execute(".mode table")
#c.execute(".mode box")

c.execute("DROP TABLE IF EXISTS courses;") # deletes any existing "courses" tables so when we create a new one we don't run into an error
c.execute("create table courses(code text, mark int, id int);") # test SQL stmt in sqlite3 shell, save as string


#==========================================================

with open("courses.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    #populates table by inserting values
    for row in reader:
        c.execute("insert into courses values('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");")

c.execute("select * from courses;")

#==========================================================

c.execute("DROP TABLE IF EXISTS students;") # deletes any existing "students" tables so when we create a new one we don't run into an error
c.execute("create table students(name text, age int, id int);") # test SQL stmt in sqlite3 shell, save as string

#==========================================================

with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    #populates table by inserting
    for row in reader:
        c.execute("insert into students values('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");")

c.execute("select * from students;")

#==========================================================

db.commit() #save changes
db.close()  #close database