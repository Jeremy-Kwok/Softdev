# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from tkinter.ttk import Style
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True 
    app.run()