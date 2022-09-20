#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

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