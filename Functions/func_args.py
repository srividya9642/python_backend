# Python function Arguments :
'''Function arguments are the values or data that we pass to a function when calling it.

They allow us to send information into the function so it can perform operations using that data.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.

'''
# Example :
def my_function(fname):
    print(fname + 'refsnes')
    
my_function('Emil')
my_function('Tobias')
my_function('Linus')


# parameters vs Arguments :

# The terms parameters and arguments can be used for the same thing:
# Information that are passed into a function.abs

# parameter : A parameter is the variable listed inside the parantheses in the function definition.
# Argument : A argument is the actual value that is sent to the function when it is called.
def my_function(name):    #name is a parameter
    print("hello",name)
    
my_function('srividya')  # srividya is a argument



# Number of Arguments :
''' By default, as function must be called with the correct number of Arguments.
if our function expects 2 arguments, we must call it with exactly 2 arguments. '''

def my_function(fname, lname):
    print(fname + " " + lname)
    
    
my_function("srividya","bellamkonda")
    
    
    
# Default parameter values :
''' we can assign default values to parameters. if the function is called without an argument, it uses the default value:'''

def my_function(name = 'friend'):
    print('hello',name)

my_function('sri')
my_function('vidya')
my_function()
my_function('srividya')

# Example : Default value for country parameter :
def my_function(country = 'norway'):
    print('I am from', country)
    
my_function('Delhi')
my_function('Brazil')
my_function()
my_function('India')



# Keyword Arguments() : we can send arguments with the key = value syntax.

def my_function(animal, name):
    print("I have a", animal)
    print('My', animal + " 's name is", name)
    
my_function(animal = 'dog', name = 'Buddy')

# This way, with the keyword arguments, the order of the arguments does no matter.abs

def my_function(animal, name):
    print("I have a ", animal)
    print("My",animal + "'s name is", name)
    
my_function(name = 'Buddy', animal = 'Dog')


# Positional arguments :
''' When we  call a fucntion with arguments without using the keyword, they are called positional arguments.

positional arguments must be in the correct order. '''

# Example :
def my_function(animal, name):
    print("I have a",animal)
    print("My", animal + "'s name is", name)
    
my_function('Dog', 'Buddy')

#  The order matters with the postional arguments, switching the order woth positional arguments.
def my_function(animal, name):
    print("I have a" ,animal)
    print("My", animal +"'s name is", name)
    
my_function('Buddy', 'Dog')



# Mixing positional and keyword arguments :
''' we can mix positional and keyword arguments in a function call.

However, positional arguments must come before keyword arguments: '''
def my_function(animal, name, age):
    print("I have a",age, "Year old", animal, "named",name)
    
my_function('dog', name = 'Buddy',age = 5)


# Passing different data types : We cannsend any data type as an argument to a function(string, number,list,dictionary,etc.)

# The data type will be preserved inside the function:

def my_function(fruits):
    for fruit in fruits:
        print(fruit)
    
my_fruits = ['apple','banana','cherry']   
my_function(my_fruits)


# sending a dictionary as an argument :
def my_function(person):
    print('Name:',person['name'])
    print('Age:', person['age'])

my_person = {'name':'Emil', 'age': '22'}
my_function(my_person)



# Return values :  Functions can return values using the 'return' statement :

def my_function(x,y):
    return x + y

result = my_function(5,3)
print(result)



# Returning Different Data Types: Functions can return any data type, including lists, tuples, dictionaries, and more.

def my_function():
    return['apple','banana','cherry']

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# returning a tuple :
def my_function():
    return(10,20)
x,y =  my_function()
print('x:',x)
print('y:',y)


# Positional-only Arguments :
''' we can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add, / after the arguments:'''

def my_fucntion(name,/):
    print('Hello', name)
    
    
    
my_fucntion('Emil')


''' without, / we are actually allowed to use keyword arguments even if the function 
expects positional arguments '''

def my_function(name):
    print("Hello", name)
    
my_function(name = 'Emil')


# with ,/, we will get an error if we try to use the keyword arguments :

def my_function(name,/):
    print("Hello", name)
    
my_fucntion(name = 'Srividya') # Error



# Key-word only arguments: To specify that a function can have only keyword arguments, add *, before the argument:
def my_function(*, name):
    print("Hello", name)
    
my_fucntion(name ='Emil')


# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:
def my_function(name):
    print("Hello", name)
    
    
my_function('Emil')


# Combining Positional-only and keyword-only
''' we can combine both argument types in the same function.
Arguments before / are positional-only, and arguments after * are keyword-only:'''

def my_function(a,b,/,*,c,d):
    return a + b + c + d

result = my_function(5,10,c = 15, d = 20)
print(result)