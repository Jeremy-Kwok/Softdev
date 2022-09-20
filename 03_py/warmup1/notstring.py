#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    if str[0:3] != "not" :
        return "not " + str
    else:
        return str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))