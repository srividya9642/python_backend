# removing empty tuples from a list-python
# using list comprehension :
a = [(1,2),(),(3,4),(),(5,)]
res = [t for t in a if t]
print(res)

# using filter()
''' filter() is s functional programming approach to remove empty tuples from a list.
Using none as the first argumenet automatically filters out all falsy values, including 
empty tuples because empty tuples evaluate toFalse in python.'''


a = [(1,2),(),(3,4),(),(5,)]
res = list(filter(None, a))
print(res)


# Using 
