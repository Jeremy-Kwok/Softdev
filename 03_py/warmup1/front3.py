def front3(str):
    front = 3
    if len(str) < 3:
        front = len(str)
    beginning = str[0:front]
    return beginning + beginning + beginning

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))