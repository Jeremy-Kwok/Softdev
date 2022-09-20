#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    newstring = ""
    for n in range (0, len(str)+1):
        newstring += str[0:n]
    return newstring

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))

