# CDDN - Jeremy Kwok, Brianna Toe, Jun Hong
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # Print whatever __name__ is in the terminal
    return "No hablo queso!"  # ...

app.run()  # ...
                
'''
Expected Behaviors:
    -A new page opens up with "No hablo queso!" at the center of the page

Actual Behaviors:
    -The first time we run the file, a link to the website is printed into the terminal, with nothing popping up in our browser.
    
     * Serving Flask app 'app'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    
    "__main__
    127.0.0.1 - - [Date/Month_Abbreviation/Year Hour:Minute:Second] "GET / HTTP/1.1" 200 -"
    -A message like this one (with the current date and time) is printed in the terminal EVERY time the website is refreshed/reloaded

    "127.0.0.1 - - [05/Oct/2022 21:04:09] "GET /favicon.ico HTTP/1.1" 404 -"
    -This line follows the "__main__" lines (ONLY after the website is initially created)
'''