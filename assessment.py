# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def item_total_cost(state, item_cost, tax=.05):
    """
    Function takes in 3 parameters (tax parameter is set to .05 as default).
    Returns the total cost of the item (including tax).
    If state == CA then it changes the default tax parameter to .07 and returns
    the total cost of the item (including a .07 tax)
    """
    state = state.upper()
    print state
    if state == 'CA':
        tax = .07
        print tax
        return item_cost + (item_cost * tax)
    else:
        return item_cost + (item_cost * tax)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".


def is_berry(fruit_type):
    """
    Checks if fruit type submitted is strawberry, cherry or blackberry and returns True.
    If any other fruit is submitted, empty string or a number is given it returns False.
    """
    fruit_type = fruit_type.lower()  # turns fruit_type string into all lowercase
    if fruit_type == "strawberry" or fruit_type == "cherry" or fruit_type == "blackberry":
        return True
    elif fruit_type.isdigit() is True or len(fruit_type) < 3:  # checks if a number was given in the string, empty string or insufficient letters were given
        return "Nice try! Please enter a fruit type."
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit_type):
        """
        Returns shipping cost depending on fruit_type given.
        """
        if is_berry(fruit_type) is True:
            return 0
        else:
            return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(town_name):
    """
    Checks if hometown is given as a parameter, if so returns 'True'
    """
    if town_name.lower() == "windsor":
        return True
    elif town_name.isdigit() is True:
        return False
    else:
        return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    return "%s %s" % (first_name, last_name)
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(hometown, first_name, last_name):
    """
    Takes hometown, first and last name as parameters, then evaluates if hometown is the same
    as the one outlined in the is_hometown() function. If that function returns True it prints
    a message letting know the person we're from the same place. Else it asks where the person is from.

    Makes use of the full_name() function as well when printing out message.
    """
    if is_hometown(hometown) is True:
        print "Hi, %s, we're from the same place!" % (full_name(first_name, last_name))
    else:
        print "Hi %s, where are you from?" % (full_name(first_name, last_name))


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

"""
In order for the add() function to have access to the variables to do the math you
need to pass them in the outer function. For this reason I made the outer function
take in the 2 parameters (including the optional one), then created a separate function
to do the math and called it to return the value.
"""


def increment(number1, number2=1):
    def add():
        return number1 + number2
    return add()

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

"""
I think this is what the question wanted? You can't call a variable as far as I know. You can only call a function.
Created the addfive() function with one parameter, then called the increment() function in there with the optional
parameter already set to 5.
Called the addfive() function with the 2 different values by printing it below.
"""


def addfive(test_number):
    return increment(test_number, number2=5)

print addfive(5)
print addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def extending_list(number, list_of_numbers):

    if type(number) == int:
        list_of_numbers.append(number)
        return list_of_numbers
    else:
        return "Nice Try! Please enter a number to add to the list."

#####################################################################
