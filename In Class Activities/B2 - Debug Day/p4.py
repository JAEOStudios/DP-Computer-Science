#the goal of this program is to sum all of the digits of a user inputted number together
#getting input
x = int(input("Please enter a number: "))
sum = 0
#looping while the number still has digits
while x > 0:
    sum = x % 10
    x /= 10
#printing the sum
print(sum)

