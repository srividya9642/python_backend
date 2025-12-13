# Loop through a Tuple : we can loop through the tuple items using a 'for' loop.abs
# ex : iterate through the items and print the values :



thistuple = ('apple','banana','cherry')
for items in thistuple:
    print(items)
    
    
    
# Loop through the index numbers :
''' we can alos loop trough the tuple items by referring to their index numbers.
Use the range() and len() functions to create a suitable iterable. '''
# ex : print all items by referring to their index numbers:

thistuple = ('apple','banana','cherry')
for i in range(len(thistuple)):
    print(thistuple[i])
    
    
    
# Using a while loop :  print all items using 'while' loop to go through all the index numbers.abs
thistuple = ('apple','banana','cherry')
i = 0

while i < len(thistuple):
    print (thistuple[i])
    i = i+1 
