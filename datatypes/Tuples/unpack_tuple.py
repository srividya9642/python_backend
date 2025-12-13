# Unpacking a tuple :
''' when we create a tuple, we normally assign values to it. This is called packing a tuple.'''

# ex :

fruits = ('apple','banana','cherry')
print(fruits)

# but in python, we were also allowed to extract the values back into variables, This is called "unpacking" :


# Ex : unpacking a tuple :
fruits = ('apple','banana','cherry')
(green,yellow,red) = fruits

print(green)
print(yellow)
print(red)


''' Using Asterisk :

 If the no of variavle is less than the no of values, we can add an * to the variable
 name and the values will be assigned to the variable as a list : '''
 
 
fruits = ('apple','banana','cherry','strawberry','raspberry')
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) 


# If the asterisk is added to another variable name than the last, Python will assign values
# to the variable until the number of values left matches the number of variables left.


# ex : add a list of values the 'tropic variable :

fruits = ('apple','mango','papaya','pineapple','cherry')
(green, *tropic,red) = fruits
print(green)
print(tropic)
print(red)