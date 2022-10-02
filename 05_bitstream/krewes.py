'''
Just Kidding Apple Kids: Jeremy Kwok and Anjini Katari
SoftDev
DUO MISSION
2022-09-28
time spent: 1.0 hour

DISCO
    -.append() adds an object to the end of a list
    -.read() will read an imported file
    -.split() divides the file into a list by whatever argument you put in 

QCC
    -similar variable names are very confusing and annoying
    -why do we need to specify to read a file AFTER we import the file? Why can't it just automatically read it after we put 'r' for reading rights?

OPS SUMMARY
    sort()
    -Splits krewes.txt using @@@, and then runs each part through obtain_devo_ducky(devo_info)

    obtain_devo_ducky(devo_info)
    -Splits devo_info by $$$, and then omits period and returns devo name and ducky name separated by a comma

    choose()
    -Randomly chooses a period, and devo-ducky pair

'''

krewes_file = open("krewes.txt", 'r')
content = krewes_file.read()
import random as rng

krewes = {2:[], 7:[], 8:[]}

def sort():
    pd_devo_ducky = content.split("@@@")

    for n in pd_devo_ducky:
        if n[0] == '2':
            krewes[2].append(obtain_devo_ducky(n))
        
        if n[0] == '7':
            krewes[7].append(obtain_devo_ducky(n))

        if n[0] == '8':
            krewes[8].append(obtain_devo_ducky(n))

    return krewes

def obtain_devo_ducky(devo_info):
    spliter = devo_info.split('$$$') #Splits devo_info, which includes the period, devo name, and ducky name
    devo_ducky = spliter[1:] #stores the devo name and ducky name in a list
    return devo_ducky

def choose():
    period = rng.choice([2, 7, 8]) #choose a random period
    devo_ducky_pair = rng.choice(krewes[period]) #choose a random devo_ducky pair
    devo = devo_ducky_pair[0] #picks out devo from devo_ducky pair
    ducky = devo_ducky_pair[1] #picks out ducky from devo_ducky pair

    output = devo + " and Ducky " + ducky + " from period " + str(period)
    return output

sort()
print(choose())
