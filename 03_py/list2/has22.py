#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere

def has22(nums):
    previousnumberwas2 = False
    for x in nums:
        if x == 2 and previousnumberwas2:
            return True
        if x == 2:
            previousnumberwas2 = True
        else:
            previousnumberwas2 = False
    return False

print(has22([1, 2, 2])) # True
print(has22([1, 2, 1, 2])) # False
print(has22([2, 1, 2])) # False