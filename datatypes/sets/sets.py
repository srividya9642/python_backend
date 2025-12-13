# set()
''' 1.set is a collection of unique items.
2. set is defined by the values separated by comma(,)
inside the {}.
3. items in a set are not ordered, since sets are not ordered, indexing has no meaning.
4. it is used to store multiple items in a single variable,similar to list or tuples, but with no
duplicate values.
5. sets are mutable meaning, we can add or remove elements after creation.
6. Since sets are unordered, the items do not have an index, so we can not access them by position. '''

# Unordered : unordered means that the items in a set do not have a defined order.
# set items can appear in a different order every time we use them,and cannot be referred by index or key.


# unchangable : Set items are unchangable, meaning that we cannot change the items after the set has been created.

# Once a set is created , you cannot change its items, but we can remove items and add new items.


#Duplicates Not Allowed ; Sets cannot have two items with the same value .

# ex : Duplicate values will be ignored.

thisset = {'apple','banana','cherry','apple'}
print(thisset)


#ex :2 
thisset = {'apple','banana','cherry',True,1,2}
print(thisset)

# ex3 :
thisset = {'apple','banana','cherry',False,True,0}
print(thisset)



# Get the length of a set :
thisset = {'apple','banana','cherry'}
print(len(thisset))


# Set items - Data types, set items can be of any data type ;
set1 = {'apple','banana','cherry'}
set2 = {True,False,True}
set3 = {1,2,3,4,5}

print(set1)
print(set2)
print(set3)



thisset = {'aba',34,True,40,'male'}
print(type(thisset))


# using the set constructor to make a set :
thisset =set (('apple','banana','cherry')) # Note the double rounded brackets
print(type(thisset))


