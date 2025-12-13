# Pass Statement :
''' we use the pass statememnt in python to write empty loops, pass is also
used for empty control statements, functions and classes


The pass statement is a place holder that does nothing when executed.
* it is used to keep code blocks valid where a statement is requires but no logic is needed yet.
* Examples situations where pass is used are empty functios, classes, loops or conditional blocks.

'''


# In functions:  the pass keyword in a functions is used when we define a function but don't want to implement
# its logic immediately. It allows the function to be syntactically valid. even though it doesn't perform any actions yet.



def fun():
    pass

fun()  # call the function
# No output



# In conditional statements;
''' Sometimes we using  "conditional statements" we may not want to perform any actions for a second conditon
but still need the block to exist. The pass statement ensures the code remains valid without adding logic.'''

x = 10

if x > 5 :
    pass  # place holder for future logic
else:
    print("x is 5 or less")
    
    
    
# In Loops:
''' In loops , pass can be used to skip writing any action during a specific iteration while still keeping the loop 
structure corect'''


for i in range(5):
    if i ==3 :
       pass     # Do nothing when i is 3
    else :
        print(i)
        
        
        
# In classes :
''' The pass statement allows dfiniting empty classed or methods that acts as
placeholders until actual functionality is added later.'''


class EmptyClass:
    pass # No methods or attributes yet

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        pass  # placeholder for greet method
    
# creating an instance of the class
p = person("Emily", 30)
    
