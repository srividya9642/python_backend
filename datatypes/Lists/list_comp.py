# List comprehension:


''' List comprehension is a concise way to create lists using a single line of code. It is useful for applying 
an operation or filter to items in an iterable, such as list or range.'''


squares = [x**2 for x in range(1,6)]
print(squares)


l = [2 ** i for i in range(int(input("Enter a number")) +1)]
print(l)



# ex2 ..
thislist = ["apple","orange","banana"]
newlist = []

for x in thislist:
  if 'a' in x :
      newlist.append(x)
print(newlist)

# one line of code :

thislist = ["apple","orange","banana"]
newlist = [x for x in thislist if 'a' in x]
print(newlist)


# condition : The condition is like a filter that only accepts the items that  evaluate to "True".abs
thislist = ["apple","orange","banana"]
newlist = [x for x in thislist if x != 'apple' ]
print(newlist)


# the above condition if x != 'apple' will return 'True' for all elements other than 'apple',
# making the new list contain all fruit except 'apple'.

thislist = ["apple","orange","banana"]
newlist = [x for x in thislist]
print(newlist)




# Iterable : The iterable can be any iterable object, like a list, tuple, set etc..

# ex : using a range() func to create an iterable.

newlist = [x for x in range(10)]
print(newlist)


# with condition :
newlist = [ x for x in range(10) if x < 5]
print(newlist)


# expression : 
''' The expression is the current item in the iteration, but it is also the outcome, 
which we can manipulate before it ends up like a list item in the new list.'''


# Exampl : Set the values in the new list to upper case;

thislist = ["apple","orange","banana"]
newlist = [x.upper() for x in thislist]
print(newlist)


thislist = ["apple","orange","banana"]
newlist = ['hello' for x in thislist]
print(newlist)


# The expression can also  have conditions, not like the filter, but as a way to manipulate the outcome:


# Return 'orange' instead of 'banana' :
thislist = ["apple","orange","banana"]
newlist = [x if x!='banana'else 'orange' for x in thislist]
print(newlist)