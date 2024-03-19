# Functions that are from python

print("Hello World!")


# But we can make our own functions

def multiply_by_three(val):
    return 3 * val


print(multiply_by_three(3))

a = [1, 2, 3]


def append_four(my_list):
    my_list.append(4)


append_four(a)
print(a)
