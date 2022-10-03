'''
JKL: Jeremy Kwok, Kevin Li, Lauren Lee
SoftDev
Flask
2022-10-03
time spent: .5 hours (in-class time)
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print("hello") # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. java
1. current directory, run whatever is in the route
2. every time reloaded, whatever is in the print function is printed in the terminal
3. __main__
4. prints on webpage
5. java
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''