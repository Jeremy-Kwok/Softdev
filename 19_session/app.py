# Jelly Jam Pancakes - Jeremy Kwok, Jacob Guo, Prattay Dey
# SoftDev
# 2022-11-06
# time spent: 1.0

#Username: Pancake
#Password: Syrup

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

required_username = "Pancake"
required_password = "Syrup"


@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    '''
    return render_template('login.html')


@app.route("/login", methods=['GET', 'POST'])
def authenticate():
    
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    '''

    #Use this to force a post request
    print("***DIAG: request.form ***")
    print(request.form)
    #print(request.args['username'] + request.args['sub1'])
    #return render_template('response.html')
    #print(request.form)



    if request.method == 'GET':
        input_username = request.args['username']
        input_password = request.args['password']
        if input_username == required_username and input_password == required_password:
            print("SUCCESS")
            return render_template('response.html', username = request.args['username'], password = request.args['password'], method = request.method)  #For 'get'
        elif input_username != required_username and input_password == required_password:
            print("username not recognized")   
            return render_template('login.html')
        elif input_username == required_username and input_password != required_password:
            print("incorrect password")   
            return render_template('login.html')
        else:
            print("Seems like you don't know the username OR password. Are you an imposter?")
            return render_template('login.html')
    

    if request.method == 'POST':
        input_username = request.form['username']
        input_password = request.form['password']
        if input_username == required_username and input_password == required_password:
            print("SUCCESS")
            return render_template('response.html', username = request.form['username'], method = request.method)  #For 'post'
        elif input_username != required_username and input_password == required_password:
            print("username not recognized")   
            return render_template('login.html')
        elif input_username == required_username and input_password != required_password:
            print("incorrect password")  
            return render_template('login.html') 
        else:
            print("Seems like you don't know the username OR password. Are you an imposter?")
            return render_template('login.html')
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
