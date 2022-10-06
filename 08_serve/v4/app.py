# CDDN - Jeremy Kwok, Brianna Toe, Jun Hong
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

'''
Expected Behaviors:

    -Initial run message printed to the terminal:

         * Serving Flask app 'app'
         * Debug mode: on
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         * Running on http://127.0.0.1:5000
        Press CTRL+C to quit
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 103-671-524
        
    -After the "Press CTRL+C to quit line" on each run:
        -Prints 

            the __name__ of this module is......
            __main__
            127.0.0.1 - - [Date/Month_Abbreviation/Year Hour:Minute:Second] "GET / HTTP/1.1" 200 -

        in the terminal

    -After any change and save to the file (even if it's a comment):

         * Detected change in '/Users/jeremykwok/Desktop/Softdev/00_flask/v4/app.py', reloading
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 103-671-524
    
    is printed into the terminals

Actual Behaviors:

    -Website looks exactly the same as all the other versions
    -Prints the expected initial run message
    -On each run:
        -Prints 

            the __name__ of this module is......
            __main__
            127.0.0.1 - - [Date/Month_Abbreviation/Year Hour:Minute:Second] "GET / HTTP/1.1" 200 -

        in the terminal
    
    -After any change and save:

         * Detected change in '/Users/jeremykwok/Desktop/Softdev/00_flask/v4/app.py', reloading
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 103-671-524
    
    is printed into the terminal

'''