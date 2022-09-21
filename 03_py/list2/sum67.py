#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
    ignore = False
    sum = 0
    for x in nums:
        if (x == 6):
            ignore = True
        if not ignore:
            sum = sum + x
        if (x == 7):
            ignore = False
    return sum

print(sum67[1, 2, 2]) # 5
print(sum67[1, 2, 2, 6, 99, 99, 7]) # 5
print(sum67[1, 1, 6, 7, 2]) # 4