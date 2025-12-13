# In python tuple has two built-in methods that we can use.

# count() : The count() method returns the no of times a specified value appears in the tuple.abs
# Syntax : tuple.count(value)

# Example : return the no of times the value 5 appears in the tuple ;

thistuple = (1,3,7,8,7,5,4,6,8,5)

x = thistuple.count(5)
print(x)



# index() : the index method finds the first occurance of the specified value.
# index() : method raisess an exception if the value is not found.

thistuple =  (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)