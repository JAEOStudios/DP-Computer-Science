#code to detect if a string is a palindrome
word = input("Type in a word to see if it's a palindrome.")
isPalindrome = True
for i in range(0,len(word)):
    if(word[i] == word[len(word)-1]):
        isPalindrome = True
    else:
        isPalindrome = False
if isPalindrome:
    print("Is a palindrome.")
