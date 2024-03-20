from decimal import Decimal, getcontext

# You can also cast a string to a int

a = int('100')
print(a)

a_1 = int('100', 2)
print(a_1)

# Floating errors

a_2 = 1.2 - 1.0
print(a_2)

# Decimal import

get = getcontext().prec = 2
print(Decimal(1) / Decimal(3))

get_2 = getcontext().prec = 3
print(Decimal(1) / Decimal(3))


print(Decimal(3.14))
print(Decimal('3.14'))

