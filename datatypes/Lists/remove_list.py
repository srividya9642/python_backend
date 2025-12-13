# Remove list items ;
# remove specified items :
# remove () ; the remove () method removes the specified values from the list.


thislist = ["apple","banana","orange","kiwi","cherry"]
thislist.remove("cherry")
print(thislist)


# pop() : The method pop will remove the specified index, which means it will the remove the element which we specified in index.

thislist = ["apple","banana","orange","kiwi","cherry"]
popped_list = thislist.pop(1)
print(popped_list)
print("After popped :" ,thislist)

# remove the element from  the list without specifying the index :
thislist = ["apple","banana","orange","kiwi","cherry"]

thislist.pop()
print(thislist)



# del() keyword is also remove the specified index :

# example ;

thislist = ["apple","banana","orange"]
del thislist[0]
print(thislist)

# >> The del () keyword can also delete the complete list :
thislist = ["apple","orange","banana"]
del thislist


# clear() method : the method clear will empties the lsit,The list still remain but it has not content.

thislist = ["apple","orange","banana"]
thislist.clear()
print(thislist)
