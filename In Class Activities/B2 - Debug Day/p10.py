#function to return the index of a specific number in list
#return -1 if not found
def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            return -1

#calling the function
print(find_index([5, 7, 9, 11], 11))