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

print(sort())
print(choose())
