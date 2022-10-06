'''
CDN: Jeremy Kwok, Brianna Toe, Jun Hong
SoftDev
serve
2022-10-05
time spent: 0.4 hours on app.py, 1.0 hours on v0-v4

'''

import random as rng
occupations_file = open("occupations.csv", 'r')
content = occupations_file.read()

from flask import Flask 
app = Flask(__name__) # ...

'''
1. Build dictionary (keys are occupation names and values are percentages IN NUMBERS)
'''

occ = {}

def sort():
    spliter = content.split("\n")
    spliter = spliter[1:23] #removes the first and last element of the spliter

    for n in spliter:
        reverse = n[::-1] #reverses the order of characters and numbers
        #print(reverse)

        slicer = reverse.split(",", 1) #splits reverse by the first comma
        #print(slicer)

        job = slicer[1] #sets job to the second element of slicer
        percentage = slicer[0] #sets percentage to the first element of slicer

        job = job[::-1] #flips the order of characters in job
        #print(job)

        percentage = float(percentage[::-1]) #flips the order of percentage, and turns it into a float
        #print(percentage)

        occ[job] = percentage #adds job and percentage to dictionary

sort()


'''
2. Create a function that selects a random occupation (based on weight of percentage)
    1. add up the percentages
    2. pick random value
    3. if random value falls into percentage range of a job, pick that job
'''

def picker():
    rand = rng.uniform(0.0,99.8) #picks a random float from 0 to 99.8 (hopefully inclusive)
    counter = 0 #sets counter to 0
    for key in occ: #for loop for each key in the occ dictionary
        counter += occ[key] #adds value of key to counter
        if counter >= rand: #if counter is larger than or equal to random value
            return key #return key associated with the value most recently added

@app.route("/") # ...
def hello_world():
    print(__name__) # Print whatever __name__ is in the terminal
    return "Chosen occupation: " + picker() # ...

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

app.run()  # ...