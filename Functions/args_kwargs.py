# python *args and **kwargs:
''' By default a function must be called with the correct number of arguments.
However,sometimes we may not know whow many arguments that will be passed into the function.

*args and **kwargs allow functions to accept unknown number of arguments.'''


# Arbitrary Arguments = *args
'''If we do not know how many arguments will be passed into  function, we can add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly.'''
def my_function(*kids):
    print("The youngest child is" + kids[2])
    
my_function("Emil","Tobias","Linus")


# what is*args?
'''The *args parameter allows a function to accept any number of positional arguments.

Inside the function, args becomes a tuple containing all the passed arguments: '''

def my_function(*args):
    print("Type:",type(args))
    print("First arguments:",args[0])
    print("Second argument:",args[1])
    print("All arguments:", args)

my_function("Emil","Tobias","Linus")
