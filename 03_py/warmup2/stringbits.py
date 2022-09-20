#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    newstring = ""
    for n in range (0, len(str)):
        if n % 2 == 0:
            newstring += str[n]
    return newstring

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))