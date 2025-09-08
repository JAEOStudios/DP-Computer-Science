#guess the secret number game
secret = 7
#getting input
guess = int(input("Guess a number: "))

#looping until the get the number
while guess == secret:
    guess = int(input("Wrong! Guess again: "))

print("You got it!")