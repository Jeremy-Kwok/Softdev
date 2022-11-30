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
    f = open("key_cat.txt", "r")
    key = f.read()

    x = requests.get('https://api.thecatapi.com/v1/images/search?api_key=' + key)
    print(x)
    print(x.request)
    print(x.json())
    #print(x.content)
    json = x.json()[0]
    id = json['id']
    image = json['url']
    breeds = json['breeds']
    #answer = json["answer"]
    print(image)

    return render_template("index.html", id = id, image = image, breeds = breeds)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()