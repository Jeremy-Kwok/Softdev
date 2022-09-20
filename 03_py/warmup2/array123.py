def array123(nums):
    for n in range (0, len(nums)-2):
        if nums[n] == 1 and nums[n+1] == 2 and nums[n+2] == 3:
            return True
    return False

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
