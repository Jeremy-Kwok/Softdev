#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
    for n in range (0, len(nums)):
        if nums[n] == 2 or nums[n] == 3:
            return True
    return False

print(has23([2, 5])) # True
print(has23([4, 3])) # True
print(has23([4, 5])) # False