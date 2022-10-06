# CDDN - Jeremy Kwok, Brianna Toe, Jun Hong
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
Expected Behaviors:
    -Does everything v0 does but doesn't print __main__ in the terminal

Actual Behaviors:
    -New website does not prompt my google translate to ask if I want spanish-to-english translation on first run
    -Does not print __main__ to terminal when program is run
    -Does everything else like v0

'''