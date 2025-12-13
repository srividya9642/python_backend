#Dictionary :
''' 1. Dictionaries in python is ordered collection of key,value pairs.
2. is is generally used when we have a huge amount of data.
3. dictionaries defined in curly{} brackets where each item being paired as keys and values.
4. we also called the dictionaries as mapping data types , as they map keys to values.
5. Dictionaries are mutable, which means we can change add , remove the elements once we create.'''


# Example :
thisdict = {
    'brand':'Ford',
    'model':'mustang',
    'year': 1964
}

print(thisdict)

# Dictionary items :
''' Dictionary items are ordered, changable, and do not allow duplicates.
Dictionary items are presented in key:value pairs,and can be referred to by using the key name.'''

# Print the 'brand' value of the dictionary:

thisdict = { 
    'brand' : 'Ford',
    'model' : 'mustang',
    'year' : 1964
}

print(thisdict['brand'])


# Duplicated are not allowed : Dictionaries cannot have two items with the same ket;
# duplicate values will overwriting existing values :

thisdict = {
    'brand' :'Ford',
    'model' : 'mustang',
    'year' : 1964,
    'year': 2020
}

print(thisdict)



# Dictionary length : To determine how many items a dictionary has, we can use the len() function:

thisdict = {
    'brand': 'Ford',
    'model' : 'mustang',
    'year' : 1964
}

print(len(thisdict))


# Dictioary items - Data Types
# the values in dictionary can be of any data type;

thisdict = {
    'brand' : ' Ford',
    'electric' : False,
    'year' :1964,
    'colors' : ['red','white','blue']
    
}
print(thisdict)


# Type () : From Python's perspective, dictionaries are defined as objects with the data type 'dict':

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
print(type(thisdict))


# The dict() constructor : It is also possible to use dict(). constructor to make a dictionary.abs

thisdict = dict(name = 'John', age = 36, country = 'Newdelhi')
print(thisdict)