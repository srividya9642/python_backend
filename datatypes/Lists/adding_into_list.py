# We can add elements to a list using the following methods:


# append():  Adds an element at the end of the list.
# extend():  Adds multiple elements to the end of the list.
# insert():  Adds an element at a specific position.




a = []


a.append(10)
print("After append(10):", a)

a.insert(0,5)
print("After insert(0,5):", a)

a.extend([15,20,25])
print("After extend ([15,20,25]):", a)

a.clear()
print("After clear():", a)




# Add any iterable :
''' The extens method does not have to append the list, we can add any iterable objects(tuples,sets,dictionaries etc.)'''

thislist = ["apple","banana",'cherry']
newtuple = ("kiwi","orange")
thislist.extend(newtuple)
print(thislist)





# Updating elements into list : Since lists are mutable, we can update elements by accessing them via their index.

a = [10,20,30,40,50]
a[1] = 25
print(a)

fruits = ['apple','banana','cherry']
my_tuples = ('orabge','grapes')
fruits.append(my_tuples)
print(fruits)

fruits = ['apples','banana','cheery']
vegetables = ['brinjal','tomato','onion']
fruits.extend(vegetables)
print(fruits)