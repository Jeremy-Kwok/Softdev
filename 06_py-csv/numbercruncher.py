'''
Just Kidding Apple Kids: Jeremy Kwok and Anjini Katari
SoftDev
Divine your Destiny!
2022-10-02
time spent: 2 hours

DISCO
    -.pop(index) removes the element at the specificed index from the list and returns it. If no index is provided, it defaults to the last element in the list
    -rng.uniform(x,y) returns a random float between x and y

QCC
    -What/Where is the remaining 0.2%?


HOW THIS SCRIPT WORKS
    sort()
        -splits the file by each new line and makes it into a list
        -removes the first and last elements of the list
        -reverse each element
        -separates it into two elements by comma
        -take the second element in the sublist as job
        -take the first element in the sublist as percentage
        -reverse the order of characters in job and percentage
        -change percentage from a string to a float
        -add job : percentage to dictionary

    picker()
        -picks a random float from 0 to 99.8 (hopefully inclusive)
        -sets counter to 0
        -loop through each key in the occ dictionary
        -adds value of key to counter
        -if counter is larger than or equal to random value, then return key associated with the value most recently added
'''

occupations_file = open("occupations.csv", 'r')
content = occupations_file.read()
import random as rng

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

print(occ)
print("Chosen occupation: " + picker())

