# Team Jelly Jam Pancakes: Jacob, Jeremy, Prattay
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="courses.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

c.execute("DROP TABLE IF EXISTS courses;") # deletes any existing tables so when we create a new one we don't run into an error
c.execute("create table courses(code text, mark int, id int);") # test SQL stmt in sqlite3 shell, save as string


#==========================================================

with open("courses.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['code'], row['mark'], row['id'])
        c.execute("insert into courses values('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");")

courses_db = c.execute("select * from courses;")

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
# c.execute(command)    # run SQL statement

#==========================================================





DB_FILE="students.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

c.execute("DROP TABLE IF EXISTS students;") # deletes any existing tables so when we create a new one we don't run into an error
c.execute("create table students(name text, age int, id int);") # test SQL stmt in sqlite3 shell, save as string


#==========================================================

with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['code'], row['mark'], row['id'])
        c.execute("insert into students values('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");")

students_db = c.execute("select * from students;")

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
# c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
