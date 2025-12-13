''' we canmot access items in a set by referring to an index or a key.
but we can loop through the set items by using a "for loop", or ask if a specified 
value is present in a set, by using the 'in' keyword.'''

# loop through a set

thisset = {'apple','banana','cherry'}
for  item in thisset:
    print(item)
    
    
# Check if a specifie value is present in a set :
thisset = {'apple','banana','cherry'}
print('banana' in thisset)


# Check if specified value is NOT present in a set :
thisset= {'apple','banana','cherry'}
print('apple' not in thisset)