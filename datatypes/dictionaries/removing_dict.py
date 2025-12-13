# Removing Dictionary Items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name ;

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
thisdict.pop('model')
print(thisdict)


# The popitem() method removes the last inserted item( in versions before 3.7, a random item is removed instead):
thisdict = {
    'brand' :'ford',
    'model' : 'mustang',
    'year' : 1964
}
thisdict.popitem()
print(thisdict)


# The del() keyword removes the item with the specified key name :

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964

}
del thisdict['model']
print(thisdict)

## The del() keyword will also delete the complete dictionary.
thisdict = {
    'brand' : 'ford',
    'model': 'mustang',
    'year' : 1964
}
del thisdict
print(thisdict)


# The clear() method empties the dictionary:
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964

}
thisdict.clear()
print(thisdict)