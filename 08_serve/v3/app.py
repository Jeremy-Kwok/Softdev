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

app.debug = True
app.run()

'''
Expected Behaviors:
    -On the initial run: 
        -Prints the same message as v0 did up, except "Debug mode: on"
    
    -After the "Press CTRL+C to quit line":
        -Prints 

            about to print __name__...
            __main__
            127.0.0.1 - - [Date/Month_Abbreviation/Year Hour:Minute:Second] "GET / HTTP/1.1" 200 -

        in the terminal

Actual Behaviors:
    -Initial run message printed to the terminal:

         * Serving Flask app 'app'
         * Debug mode: on
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         * Running on http://127.0.0.1:5000
        Press CTRL+C to quit
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 103-671-524

    has 3 new lines (the bottom three)

    -After each reload of the website:
        
        about to print __name__...
        __main__
        127.0.0.1 - - [Date/Month_Abbreviation/Year Hour:Minute:Second] "GET / HTTP/1.1" 200 -
    
    is printed into the terminal

    -After any change and save to the file (even if it's a comment):

         * Detected change in '/Users/jeremykwok/Desktop/Softdev/00_flask/v3/app.py', reloading
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 103-671-524
    
    is printed into the terminals
'''