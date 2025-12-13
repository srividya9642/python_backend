# Dictionary methods

# 1. clear() : The clear(), method removes all the elements from a dictionary.
car = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

car.clear()
print(car)

# 2. copy() : The copy() method returns a copy of the specified dictionary.

car = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

x = car.copy()
print(x)


# fromkeys() : The fromkeys() method returns a dictionary with the specfied 
# keys and the specified value.

x = ('key1','key2','key3')
y = 0

thisdict = dict.fromkeys(x,y)
print(thisdict)