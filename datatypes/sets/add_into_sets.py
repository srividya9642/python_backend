# Change items : once a set is created , we can not change its items, but we can add the new items.abs

# To add one item to a set we use add() method.abs
thisset = {'apple','banana','cherry'}
thisset.add('orange')
print(thisset)

# ADD SETS : To add items from another set into current set, use the update() method.
thisset = {'apple','banana','cherry'}
tropical = {'pineapple','mango','papaya'}
thisset.update(tropical)
print(thisset)

# Add any iterable : The object in the update(). method does not have to be a set, it can be any
# iterable object(tuples, list,dictionaries etc.)

thisset = {'apple','banana','cherry'}
mylist = ['kiwi','orange']
thisset.update(mylist)
print(thisset)


