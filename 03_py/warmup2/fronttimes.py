def front_times(str, n):
    front = 3
    if len(str) < 3:
        front = len(str)
    beginning = str[0:front]
    return beginning * n

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))