# Remove Set Items : to remove an item in a set, we use the 'remove()', or the 'discard()'. method

# example :
thisset = {'apple','banana','cherry'}
thisset.remove('apple')
print(thisset)

# if the item to remove does not exist, remove() method will raise an error.abs

# by using the discard() method :
thisset = {'apple','banana','cherry'}
thisset.discard('cherry')
print(thisset)

# if the item to remove does not exist, discard() method will NOT raise an error.



''' We can also use the'pop()' method to remove an item, but this method will remove a randome item,
so we cannot be sure what item that gets removed.

The return value of the pop(). method is removed item.'''

thisset = {'apple','banana','cherry'}
x = thisset.pop()
print(x)
print(thisset)


# CLEAR()
# Using clear() method : The clear() method empties the set;
thisset = {'apple','banana','cherry'}
thisset.clear()
print(thisset)

#DEL()
# using the del() keyword, it will completely deletes the set.
thisset = {'apple','banana','cherry'}
del thisset
print(thisset) # it willraise an error as we have deleted the set completely.

