# There are several ways to join two or more sets in python.


# The union() and update() methods joins all items from both sets.
# The intersection(). method keeps ONLY duplicates.abs
# the difference(). method keeps the items from the first set that are not in the other set(s).
# the symmetric_difference(). method keeps all items EXCEPT the duplicates.


# Union() : the union method returns a new set with all items from both sets.abs

set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)


# we can use the '|' operator instead of union() method, and we will get the same result.

set1 = {'a','b','c'}
set2 = {1,2,3}

set3 = set1 | set2
print(set3)

# Join Multiple sets :
''' All the joining methods and operators cannbe used to joinmultiple sets.
when using a method. Just add more sets in the parenthesis, separated by commas :'''

# Example : join multiple sets with the union() method :

set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = {'John','Elena'}
set4 = {'apple','bananaq','cherry'}

myset = set1.union(set2,set3,set4)
print(myset)
 
 
# By using'|' operator
set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = {'John','Elena'}
set4 = {'apple','bananaq','cherry'}
 
myset = set1 | set2 | set3 | set4
print(myset)


# Join a Set and Tuple : The union() method allows us to join a set with other data type like lists or tuples.

x = {'a','b','c'}
y = (1,2,3)
z = x.union(y)
print(z)




# Update() method : The 'update()' method inserts all items from one set to another set.
# The update() methjod chnages the original set, and does not return a new set.abs

# Example
set1 = {'a','b','c'}
set2 = {1,2,3}

set1.update(set2)
print(set1)