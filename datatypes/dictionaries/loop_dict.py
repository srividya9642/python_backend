# Loop Dictionaries :
''' We can loop tgrough the dictionaries by using 'for' loop.
when looping through a dictionary, the return value are the keys of the dictionary, but there
are methods to reu the values as well. '''


thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}

for x in thisdict:
    print(x)
    
    
# print all values in the dictionary, one by one:
thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}
for x in thisdict:
    print(thisdict[x])
    
# we can also use value() method to return values of a dictionary:

thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}
for x in thisdict.values():
    print(x)


# we can also use keys() method to return values of a dictionary:
thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}
for x in thisdict.keys():
    print(x)
    
    
# loop through both keys and values, bu using the items() method.
thisdict = {
    'brand' : ' ford',
    'model' : 'mustang',
    'year' : 1964
}
for x,y in thisdict.items():
    print(x,y)