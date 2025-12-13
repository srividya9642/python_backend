# Functions in python:
'''1. In python functions are block of reusable code that performs a specific task.
2. it helps to organize programs into smaller and managable parts.
3. functions can take inputs(parameters) and return the outputs(values).
4.They are define using the 'def' keyword followed by the function name.
5.using functions makes code clead, reusable, and easy to debug.'''

# Creating a function :
# In python a function is defined by using a 'def' keyword, followed by a function name and parentheses.
def great():
    print('Hello from a function')
great()


# Function names :
''' Function names follow the same rules as variables names in python.'''
# 1.A function name must be start with a letter or underscore.
# 2. A function name can only contain letter, numbers and underscores.
# 3. Function names are case-sensitive(myFunction and myfunction are different).abs


# valid function names :
# 1. calculate_sum()
# 2._private_function()
# 3.my_function2()


# Return values :
''' Functions can send data bcak to the code that valled them using the return statement.

when function reaches a return statement, it stops executing and sends the result back : '''

# example : A function that returns a value :
def get_greeting():
    return "Hello from a function"
message = get_greeting()
print(message)

# we can use the returned value directly:
def get_greeting():
    return "Hello form a function"

print(get_greeting())



# The pass statement :
''' function definition cannot be empty. if we we need to create a function placeholder without any code, use the 'pass' statement.'''
def my_function():
    pass


