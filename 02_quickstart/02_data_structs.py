# Lists
my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)

# list of string
my_List = ["Mario", "Lazzari"]
print(my_list)

# mixed list
my_List = ["Mario", 50, False]
print(my_list)

# list of lists
my_List = [[1,2,3], ["Mario","Lazzari"]]
print(my_list)

# list size
list_size = len(my_list)
print(list_size)

# Sets
my_set = {1,2,3,4,5}
print(my_set)
size = len(my_set)
print(size)

# set elements must be unique
my_set = {1,2,3,3,4,5,5}
print(my_set)

# equality
print({1,2}=={1,2})
print({1,2}=={1,2,3})
print({3,1,2}=={1,2,3})

# Tuples: unmutable
my_tuple = (1,2,3)
print(len(my_tuple))

# Dictionaries
my_dict = {
    "apple": "A fruit",
    "bear": "Animal"
}
print(my_dict)
print(my_dict["apple"])
