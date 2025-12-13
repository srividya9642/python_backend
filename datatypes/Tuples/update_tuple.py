''' tuples are unchangable, means that we cannot change, add, or remove items once the tuple is created.
 but there are some workarounds.'''
 
 
# change Tuple values :
''' Once a tuple is created, we cannot change its values. Tuples are unchnagale or immutable as it also is called.

But there is a workaround. we cannconvert the tuple into a list, change the list and convert the list back to a tuple.'''



# ex : convert the tuple into a list to be able to change it :

x = ('apple','banana','cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(y)


# Add items :
''' since tuples are immutable, they do not have a built-in append() method.
but there are other ways to add items to a tuple. '''


# 1. convert into a list : convert the tuple into a list, add 'orange' and convert it back to tuple.abs

thistuple = ('apple','banana','cherry')
y = list(thistuple)
y.append('orannge')
y = tuple(y)
print(y)


# 2. add tuple to a tuple :  create a new tuple and add the tuple to the existing tuple.
thistuple = ('apple','banana','cherry')
y = ('orange',)
thistuple += y
print(thistuple)



# Remove items :   convert the tuple into a list, remove 'apple', and convert it back to tuple :


thistuple = ('apple','banana','cherry')
y = list(thistuple)
y.remove('cherry')
thistuple = tuple(y)
print(y)

          #(OR)
          
          
# we can delete the complete tuple by using del( ) keyword

thistuple = ('apple','banana','cherry')
del thistuple
print(thistuple)