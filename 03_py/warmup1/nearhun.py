def near_hundred(n):
    return (n >= 90 and n <= 110) or (n >= 190 and n <= 210)

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))