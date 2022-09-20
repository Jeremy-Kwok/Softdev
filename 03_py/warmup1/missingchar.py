def missing_char(str, n):
    return str[0: n] + str[n + 1: len(str)]

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))