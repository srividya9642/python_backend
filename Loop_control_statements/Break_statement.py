# Loop control statements


''' Loop control statements in python are special statements that help control the execution of loops(for or while).
They let us modify the default behavior of the loop, such as stopping it early,
skipping an iteration,or doing nothing temporarily.'''

# 1 Break statement
# 2 continue statement
# 3 pass statement

# 1 Break statement:
''' The break statement in python is used to exit or " break" out of a loop( either a for or while loop)
prematurely, before the loop has iterated through all its items or reached its condition.
When the break statement is executed. the program immediately exists the loop, and the control 
- moves to the next line  of code after the loop.'''

# Example
# using for loop
for i in range(5):
    if i == 3 :
        break    # Exist the loop when i = 3
    print(i)

# using while loop:

i = 0
while i < 5 :
     if i ==3 :
         break
     print(i)    # Exit the loop when i is 3
     i += 1


# exmple of the break
# Example: Searching for an element in a list

a = [ 1,3,5,7,9,11]
val = 7

for i in a :
    if i == val:
        print(f"Found at {i}!")
        break
else :
      print("Not found")


# Break statement with for loop :
''' The break statement can be used within a for loop to exit the loop before it has iterated
over all items, based on a specific condition.'''

# example 

for i in range (10):
    print(i)
    if i == 6 :
        break
    
    
# Break statement with while loop :
''' The break statement can be used within in while loop to exit the loop based on
dynamic conditions that may not be known beforehand.'''

# example
count = 5

while True:
    print(count)
    count -=1
    if count ==0:
        print("countdown finished")
        break   # Exit the loop


# Using break condition in Nested Loops:


''' Nested Loop                                                                                                                                                                                                 s are loops within loops, allowing for more complex iterations, such as iterating over mutl-dimensional
data structures. when using break statement within nested loops, it's essential to understand its scope.'''


# Innermost Loop Exit : A break statement will only exit the loop in which it is direcly placed(the nearest enclosing loop.)

# Exiting Mutiple Loops : To ext multiple levels of nested loops, additional stratergies are required, such as using flags
# encapsulating loops within functions.



# Example :
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
val = 5
found = False

for r in matrix:
    for n in r :
        if n == val:
            print(f"{val}  found")
            found = True
            break
    if found:
        break







