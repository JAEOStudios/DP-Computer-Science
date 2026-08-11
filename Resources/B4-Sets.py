#making sets
#using curly brackets
from PIL.ImageChops import difference

my_set = {1,2,3,4,5}
print(my_set)

#using the set() constructor
#duplicate entries will be automatically removed
my_set2 = set([1,2,3,4,4,5])
print(my_set2)

#add 6 to the set
my_set.add(6)
#remove 1 from the set
my_set.remove(1)

#checking if an item is in a set
if 2 in my_set:
    print("2 is in da set")
else:
    print("2 is not in the set")

A = {1, 2, 3, 4}
B = {3, 4, 5 ,6}

#creating a union using the bar
union_set = A | B
#creating a union using the function
union_set = A.union(B)
print(union_set)

#creating an intersection using the & sign
intersection_set = A & B
#creating a intersection using the .intersection function
intersection_set = A.intersection(B)
print(intersection_set)

#creating an intersection using the - sign
difference_set = A - B
#creating a difference set using the .difference function
difference_set2 = B.difference(A)
print(difference_set)
print(difference_set2)

#making two new sets to test subset
A = {1, 4, 7}
B = {1, 2, 3, 4, 5, 6, 7,}
#check if A is a subset of B
print(A.issubset(B))
print(A <= B)
#checking for superset
print(B.issuperset(A))
print(B >= A)
