# Lists

my_list = [1, 2, 3, 4]
print(my_list)

my_list_str = ['list', 'of', 'strings']
my_list_of_lists = [[1, 2, 3], ['a', 'b', 'c']]
print(len(my_list_of_lists))

# Sets - like a list but all elem have to be unique
# And the order does not matter in a list
my_set = {1, 2, 3, 4, 5}
type(my_set)
print(len(my_set))

my_set_2 = {1, 1, 2, 2}
print(my_set_2)

# Tuples - Order matters, and you can not append or add to tuples it has to remain the same
# Used mostly for efficiency in memory

my_tuple = (1, 2, 3)
print(len(my_tuple))

# Dictionary - keys have to be unique 

my_dict = {'apple': 'A red fruit',
           'bear': 'A scary animal'}

print(my_dict['apple'])
