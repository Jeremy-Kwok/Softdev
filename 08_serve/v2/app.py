# CDDN - Jeremy Kwok, Brianna Toe, Jun Hong
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

'''
Expected Behaviors:
    -"about to print __name__..." (Brianna thinks it's "__main__") in the terminal
    -prints "__main__" in the terminal (Brianna thinks below the previous line, Jeremy thinks on the same line)
    -Does everything the same as v0

Actual Behaviors:
    -On initial run, it prints the same message v0 does into the terminal, except nothing after "Press CTRL+C to quit"
    -On each run:

    about to print __name__...
    __main__
    127.0.0.1 - - [Date/Month_Abbreviation/Year Hour:Minute:Second] "GET / HTTP/1.1" 200 -

    is printed into the terminal

    -prompts my google translate on each run
    -Nothing happens after you make changes to and save the file
'''
