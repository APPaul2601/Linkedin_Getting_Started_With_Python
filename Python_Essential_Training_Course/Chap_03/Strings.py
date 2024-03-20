# Slicing
import math

name = 'My name is Ryan Michell'

print(name[0])
print(name[1])

print(name[0:7])
print(name[:7])

print(name[11:])

# It works the same with lists

my_list = [1, 2, 3, 4, 5]

print(my_list[2:4])


# Formatting

my_str = 'My number is: ' + str(5)

# Or

my_str_1 = f"My number is: {5}"
my_str_2 = f"My number is: {5} and double that is {2 * 5}"

my_pi_str = f'Pi is {math.pi:.2f}'
print(my_pi_str)

# Multi-line Strings

multi_line_str = '''
My string: here is my long block of strings
my text doesn't stop'''

print(multi_line_str)
