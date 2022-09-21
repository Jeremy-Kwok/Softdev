#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
    previousnumberwas13 = False
    sum = 0
    for x in nums:
        if x == 13:
            previousnumberwas13 = True
        else:
            if previousnumberwas13:
                previousnumberwas13 = False
            else:
                sum = sum + x
    return sum

print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6