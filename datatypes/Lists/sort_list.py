#sort() :  sort() method is used to arrange the elements of a list in a specific order -- either ascending(default) or descending.



# Sort list Alphanumerically :
''' List objects have a sort() method that will sort the list alphanumericall,.ascending, by default.'''

# Sort the list alphanumerically :

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort the list numerically :
thislist = [50,40,30,20,10]
thislist.sort()
print(thislist)


# Sort descending : To sort descending ,we can use the keyword argument reverse = True

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# example 2 :
thislist = [10, 20, 30, 40, 50]
thislist.sort(reverse=True)
print(thislist)


# sort the list by the length of the values ;
# A function that returns the length of the values :

def myFunc(e):
    return len(e)

cars = ["Ford","Mitsubishi",'BMW',"VW"]

cars.sort(key = myFunc)
print(cars)


# sort a list of dictionaries based on the 'year' value :
def myFunc(e):
    return e['year']
    
cars = [
    {'cars': 'ford', 'year': 2005},
    {'car' : 'Mitsubishi', 'year' : 2000},
    {'car' : 'BMW', 'year' : 2019},
    {'car' : 'VW', 'year' : 2011}
]

cars.sort(key = myFunc)
print(cars)


# sort the list by the length of the values and reversed :

def myFunc(e):
    return len(e)
    
cars = ['Ford','Mitsubishi','BMW','VW']
cars.sort(reverse = True, key = myFunc)
print(cars)
    

# customize sort function():
''' We can also customize our own function by using keyword argument "key = function".
 The function will return a number that will be used to sort the the list(The lowest number)'''
 
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)



# case Insensitive sort :
''' By default  the sort() method is case sensitive, resulting in all capital letters being
sorted before lower case letters. '''

# example
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort()
print(thislist)

# we can use built-in functions as key functions when sorting a list.
# we can use str.lower as a key function, if we want a case-sensitive sort function.

thislist = ["banana","orange","kiwi","cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse order :  What if we want to reverse the order of a list, regardless of the alphabet ?



''' the reverse() method reverses the current sorting order of the elements.'''
# Reverse the order of the list items ;
thislist = ["banana","orange","kiwi","cherry"]
thislist.reverse()
print(thislist)
 
