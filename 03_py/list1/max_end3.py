#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
    if nums[0] >= nums[len(nums)-1]:
        biggerNum = nums[0]
    else:
        biggerNum = nums[len(nums)-1]
        
    for n in range (0, len(nums)):
        nums[n] = biggerNum
        
    return nums

print(max_end3([1, 2, 3])) # [3, 3, 3]
print(max_end3([11, 5, 9])) # [11, 11, 11]
print(max_end3([2, 11, 3])) # [3, 3, 3]