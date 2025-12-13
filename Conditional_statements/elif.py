''' elif statement in python stand for "else if". it allows us to
check multiple conditions, providing a way to execute
diferent blocks of code based on which condition is true.

using elif statements makes our code more readable and efficient 
by eliminating the need for multiple nested if satements.'''


# example

age = 25

if age <= 12:
    print("child.")
    
elif age <= 19:
    print("teenager.")
    
elif age <= 35:
    print("Young adult.")
else:
    print('adult')
    
    
# example 2

i = 25

if i == 10:
    print("i is 10")
elif i == 15 :
    print("i is 15")
    
elif i == 20:
    print(" i is 20")
else :
    print("i is not present")
 