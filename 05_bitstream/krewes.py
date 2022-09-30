'''
Just Kidding Apple Kids
SoftDev
DUO MISSION
2022-09-28
time spent: 

DISCO

QCC

OPS SUMMARY

'''
krewes_file = open("krewes.txt", 'r')
content = krewes_file.read()
import random as rng
krewes = {2:[], 7:[], 8:[]}

def sort():
    pd_devo_ducky = content.split("@@@")
    print(pd_devo_ducky)

    for n in pd_devo_ducky:
        if n[0] == '2':
            krewes[2].append(obtain_devo_ducky(n))
        
        if n[0] == '7':
            krewes[7].append(obtain_devo_ducky(n))

        if n[0] == '8':
            krewes[8].append(obtain_devo_ducky(n))

    return krewes

def obtain_devo_ducky(dontcare):
    spliter = dontcare.split('$$$')
    devo_ducky = spliter[1:]
    return devo_ducky

def choose():
    period = rng.choice([2, 7, 8]) #choose a random period
    devo_ducky = rng.choice(krewes[period]) #choose a random devo_ducky pair
    devo = devo_ducky[0] #picks out devo from devo_ducky pair
    ducky = devo_ducky[1] #picks out ducky from devo_ducky pair

    output = devo + " and Ducky " + ducky + " from period " + str(period)
    return output

#print(choose())
print(sort())
print(choose())
