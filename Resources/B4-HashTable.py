#Creating a hash table
hash_table = {}

#adding 2 items by key to the hash table
hash_table["key1"] = "value1"
hash_table["key2"] = 'value2'

#getting the value for key1
value = hash_table["key1"]
print("The value for 'key1' is :", value)

#deleting a key from the hash table
del hash_table["key2"]

print(hash_table)