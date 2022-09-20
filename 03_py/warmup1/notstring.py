def not_string(str):
    if str[0:3] != "not" :
        return "not " + str
    else:
        return str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))