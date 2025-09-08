#this program is intended to detect if a subword is part of a given word
word = "supercalifragilisticexpialidocious"
#getting user desired subword
subword = int(input("Enter a word that you want to check if is a subword: "))
#checking where the subword starts at if it starts at all
for i in range (0,len(subword)):
    if word[i:len(subword)] == subword:
        print("It contains it starting at character: ", i)
