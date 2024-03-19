def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    return num * factorial(num - 1)


print(factorial(5))
print(factorial(6))
print(factorial(0))
print(factorial(-2))
print(factorial(1.2))
print(factorial('spam spam spam'))
