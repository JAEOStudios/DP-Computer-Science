#program to find the X in a 2D list of strings
# #initializing the lists
list = [["A","C","B","Z","J"],
        ["U","I","J","X","O"],
        ["B","F","U","W","L"],
        ["P","O","T","L","W"],
        ["T","H","E","H","O"]]
#looping through the list
for i in range(0, len(list)):
    if list[i][i] == "X":
        print("X found at ", i, ",", i)

