#Spicy Vanilla: Jeremy Kwok
#SoftDev
#K22 -- DOG FOOD
#2022-11-28
#time spent: 1.0 hours

from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__) 

@app.route("/")       
def main():
    x = requests.get('https://yesno.wtf/api')
    print(x)
    print(x.request)
    print(x.json())
    #print(x.content)
    json = x.json()
    answer = json['answer']
    forced = json['forced']
    image = json['image']
    #answer = json["answer"]
    print(image)

    return render_template("main.html", answer = answer, forced = forced, image = image)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()