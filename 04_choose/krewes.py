'''
JKL: Jeremy Kwok, Kevin Li, Lauren Lee
SoftDev
Dictionaries and randomly accessing values
2022-09-22
time spent: .75 hours (in-class time)
DISCO
    - Typecasting something into an int is done by int(<thing you want to typecast>)
    - list() can take a dictionary parameter and return a list of keys
    - rng.choice() takes a list parameter and returns a random value in the list
    - dict.keys and dict.values return a view object, and you can't access the values in a view object using an index (ex: krewes.keys()[0] doesn't work)
QCC
    - Dictionaries are kinda like 2d arrays except the other dimension can have variables of another data type
OPS SUMMARY
    Randint:
    - Get a list of the keys in krewes
    - Take the value at a random index from 0 to 2 of the list of keys
    - Use that key to access the corresponding list and then return the devo at a random index from 0 to the length of the list - 1
    Random:
    - Same as above but using .random and typecasting instead of randint
    Choice:
    - use .choice on the list of keys
    - use .choice on the list corresponding to that key
'''
import random as rng
krewes = {2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"],
            7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
            8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }

def choose():
    #using randint
    
    keys = list(krewes)
    period = rng.randint(0,len(keys)-1) 
    period = keys[period] #randomly selects the period
    devo = rng.randint(0, len(krewes[period])-1) #randomly selects a devo from selected period
    devo = krewes[period][devo]
    

    #using random
    '''
    keys = list(krewes)
    period = keys[int(rng.random()*3)] #selects period based on a random index
    classlist = krewes[period] #takes the list of the students in that period from krewes
    devo = classlist[int(rng.random()*len(classlist)+1)] #selects a random devo from selected period
    '''

    #using choice
    '''
    period = rng.choice([2, 7, 8]) #choose a random key
    devo = rng.choice(krewes[period]) #choose a random index of the list that corresponds with the chosen key
    '''

    output = devo + " from period " + str(period)
    return output

print(choose())