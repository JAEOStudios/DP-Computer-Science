#function to sum even numbers in a list
def sum_evens(nums):
    total = 0
    for n in nums:
        if n % 2 == 1:
            total = n
    return total

#calling the function
print(sum_evens([1, 2, 3, 4]))
