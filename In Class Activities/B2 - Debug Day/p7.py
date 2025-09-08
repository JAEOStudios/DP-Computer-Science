#finding and returning the smallest number in the list
def smallest(nums):
    small = nums[0]
    for n in nums:
        if n < small:
            small = nums[0]
    return small

#calling the function
print(smallest([5, 2, 9, 1]))

