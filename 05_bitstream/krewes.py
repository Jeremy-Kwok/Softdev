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

def choose():
    keys = list(krewes)

    pd_devo_ducky = content.split("@@@")
    print(pd_devo_ducky)

    for n in pd_devo_ducky:
        if n[0] == '2':
            spliter = n.split('$$$')
            devo_ducky = spliter[1:]
            krewes[2].append(devo_ducky)
        
        if n[0] == '7':
            spliter = n.split('$$$')
            devo_ducky = spliter[1:]
            krewes[7].append(devo_ducky)
        if n[0] == '8':
            spliter = n.split('$$$')
            devo_ducky = spliter[1:]
            krewes[8].append(devo_ducky)

    print(krewes)

'''
    period = rng.choice([2, 7, 8]) #choose a random key
    devo = rng.choice(krewes[period]) #choose a random index of the list that corresponds with the chosen key

    output = devo + " from period " + str(period)
    return output
'''

#print(choose())
choose()
