#function to calculate factorial of a number
def factorial(n):
    total = 1
    #looping to calculate
    for i in range(1, n):
        total = total * i
    return total

#getting input
print(factorial(5))
