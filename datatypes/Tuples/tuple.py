# Tuple : 
''' 1.Tuples are ordered sequence of items same as list but the only difference between tuples and list 
        is lists are mutable and tuples are immutable.
    2. Tuples once created can not be changed.
    3. tuples are used to write protected data and also faster than the list because it can not dynamically changed.
    4. it is defined within paranthesis where items separated  using comma(,)'''
    
    
    # create a Tuple ;
thistuple = ("apple","banana","cherry")
print(thistuple)

# Tuple items : tuple items are ordered , unchangable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index[1] etc.


# Ordered :
''' When we say that tuples are ordered , it means that the items have a defined order,and that order will not change.'''


# Unchangable :
''' Tuples are unchangable, meaning that we cannot change,add or remove items after the tuple has been created.'''


# Allow Duplicates :
''' Since tuples are indexed, they can have items with the same values:'''
# Example ;
thistuple = ('apple','banana','cherry','apple','cherry')
print(thistuple)


# Tuple Length ;
''' To determine the number of items in the tuple :'''
thistuple = ('apple','banana','cherry')
print(len(thistuple))


# Create Tuple with one item :
''' To create a tuple with only one item, you have to add a comma after the item, otherwise python will 
not recognixe it as a tuple.'''


# Example :
thistuple = ("apple",)
print(type(thistuple))  #  correct way


thistuple = ("apple")
print(type(thistuple))


# Tuple items - Data types : tuple items can be of any data type.
# Ex

tuple1 = ('apple','banana','cherry')
tuple2 = (1,5,7,9,3)
tuple3 = (True,False,False)


print(tuple1)
print(tuple2)
print(tuple3)


# A tuple can contain different data types :

# Ex

tuple1 = ("abe",34,True,40,"Hello")
print(tuple1)



# type()
''' from python perspective , tuples are defined as objects with the data type 'tuple'.  '''
 
# example :
mytuple = ('apple','banana','cherry')
print(type(mytuple)) 
 
 
 
# The tuple constructor : It also possible to use the tuple() constructor to make a tuple.


# Ex :
thistuple = tuple(('apple','banana','cherry')) # note the double rounded brakets
print(thistuple)
