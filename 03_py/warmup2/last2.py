def last2(str):
    count = 0
    lasttwo = str[len(str)-2: len(str)]
    for n in range (0, len(str)-2):
        #print(str[n:n+2])
        if str[n:n+2] == lasttwo:
            count+=1
    return count
    
print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))