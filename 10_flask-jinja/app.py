# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
"""
A: We think it will break the test_tmplt() function, but the page will load
However, nothing will print on the next page, instead error

correction: no error, just blank page

if flask isn't open, the fields aren't loaded, so the {} aren't rendered
php?
"""
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
#A: 127.0.0.1/my_foist_template
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo") #Q2: What is the significance of each argument? Simplest, most concise answer best.
"""
A: the first one is the template file that we're trying to render, found in the templates folder
2nd argument is the title of the tab
3rd copies the coll we have to collection, then displays it?
2nd and 3rd argument fill in the gaps in the template

correction: model template isn't loaded, instead, it's used with the arguments and the path specified before the function is loaded
"""

"""
the template doesn't actually need empty fields, it just gets rendered like normal anyways
we need argument for render_template()
"""

@app.route("/fool")
def foo():
    return render_template('foo.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
