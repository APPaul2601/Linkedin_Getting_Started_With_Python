# Casting Booleans

true = bool(1)
false = bool(0)

# But any other number other than 0 is true

true_2 = bool(-1)

# Strings

true_str_1 = bool('True')
true_str_2 = bool('False')

# Lists and dict etc.

my_list = bool([])  # False
my_dict = bool({})  # False

my_list_2 = bool([1, 2])  # True

# None

none = bool(None)  # False

# Boolean logic

weather_is_nice = False
have_an_umbrella = True

if not (have_an_umbrella or weather_is_nice):
    print('Stay inside')
else:
    print('Go for a walk')

# Or you can rewrite it with an and statement

weather_is_nice = False
have_an_umbrella = True

if not have_an_umbrella and not weather_is_nice:
    print('Stay inside')
else:
    print('Go for a walk')

# The best way

weather_is_nice = False
have_an_umbrella = True

if have_an_umbrella or weather_is_nice:
    print('Go for a walk')
else:
    print('Stay inside')