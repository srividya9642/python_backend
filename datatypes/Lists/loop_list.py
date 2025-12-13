# Loop through a list : We can also loop through  the list items by using a for loop.abs
# print all the items in the list using for loop:

thislist = ["apple","orange","banana"]
for items in thislist:
    print(items)
    
    
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

# Loop through the index numbers ;
''' we can also loop through the list items by refeerring to their index numbers.by using the range() and len() functions
to create a suitable iterable'''


thislist = ["apple","orange","banana"]
for i in range(len(thislist)):
    print([i])
    
    
    
    
    
# Using while loop : We can loop through the list using while loop :
thislist = ["apple","orange","banana"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i +=1
    
    
# Loop through list comprehensions :

''' List comprehenesions offers the shortest syntax for looping through lists '''
# example :

thislist = ["apple","orange","banana"]
[print(x) for x in thislist]