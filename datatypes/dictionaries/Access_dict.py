# Accessing Dictionary items :
# We can access the dictionary items by referring to its key name, inside the square brackets.

thisdict = {
    'brand' :' Ford',
    'model' : 'mustang',
    'year' : 1964
}
x = thisdict['model']
print(x)

# There is also a method called get() that will give you the same result:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
x = thisdict.get('model')
print(x)

# Get keys : The key() method will return a list of all the keys in the directionary.

thisdict = {
    'brand' : ' ford',
    'model' : ' mustang',
    'year' : 1964
}
x = thisdict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

x = car.keys()

print(x)
car['color'] = 'white'
print(x)

# Get values : The values() method will return a list of all the values in the directionary.

thisdict = {
    'brand' : 'ford',
    'model' : ' mustang',
    'year' : 1964
}
x = thisdict.values()
print(x)

thisdict['year'] = 2020
print(x)

#2 
thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}
x = thisdict.values()
print(x)
thisdict['color'] = 'blue'
print(x)


# Get items : The items() method will return a list of all the items in the directionary.
thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}
x = thisdict.items()
print(x)
thisdict['color'] = 'white'
print(x)


# Check if key Exists :
# To determine if a specified key is present in a dictionary we use the 'in' keyword :

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
if 'model' in thisdict:
    print("yes, 'model' is one of the keys in thisdict dictionary")