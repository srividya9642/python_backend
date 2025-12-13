# Change dictioanry items : we can chnage the value of a specific item by referring to its key name:

# Example : chage the 'year' to 2018 :

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
thisdict['year'] = 2018
print(thisdict)


# Update Dictionary :
# The update(). method will update the dictionary with the items from the given argument.
# The argument must be a dictioanry, or an iterable with the key:value pairs.

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
thisdict.update({'year' : 2020})
print(thisdict)



# Update Dictionary
'''The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.'''

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
thisdict.update({'color' : 'red'})
print(thisdict)