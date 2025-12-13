# copy() ; The copy() method return a copy of the specified list.abs
# syntax : list.copy()

# ex : copy the fruits list ;
fruits = ['apple','banana','cherry','orange']
x = fruits.copy()
print(x)


# Another way to make a copy is to use the built-in method list().
# make a copy  of a list using list() method :

thislist = ['apple','banana','cherry']
mylist = list(thislist)
print(mylist)


# Use the Slice operator : we can also make copy of a list using slice(:) operator.abs


thislist = ['apple','banana','cherry']
mylist = thislist[:]
print(mylist)

