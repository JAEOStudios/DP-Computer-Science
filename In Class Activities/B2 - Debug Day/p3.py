#this code describes how many elements from list 1 appear in list 2
list = [3, 5, 19, 100, 53, 22, 89, 68, 17, 33]
list2 = [5, 99, 98, 100, 17, 2, 4, 6, 9, 0]
#finds if each element of list is found in list2
for i in range(0, len(list)):
    for j in range(i, len(list2)):
        if list[i] == list2[j]:
            print(list[j], "is a duplicate!")
