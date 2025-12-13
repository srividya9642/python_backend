''' append() : Adds an element at the end of the list.'''

# ex : 
fruits = ['apple','banana','cherry']
fruits.append('orange')
print(fruits)



''' clear() : removes all elements from the fruitslist .'''

fruits = ['apple','banana','cherry']
fruits.clear()
print(fruits)

''' copy () : returns a copy of the list '''


fruits = ['apple','banana','cherry']
fruits.copy()
print(fruits)

''' count() : returns the number of elements with the specified value.'''


fruits = ['apple','banana','cherry','apple']
x = fruits.count('apple')
print(x)

''' extend() : add the specified list elements (or any iterable) to the end of the cureent list.'''


fruits = ['apple','banana','cherry']
cars = ['Ford','BMW','Volvo']
fruits.extend(cars)
print(fruits)

''' index() : returns the index of the first element with the specified value.'''


fruits = ['apple','banana','cherry']
x = fruits.index('cherry')
print(x)

''' insert() : adds the element at the specified position.'''

fruits = ['apple','banana','cherry']
fruits.insert(1,'orange')
print(fruits)


''' pop() : removes the element at the specified position.'''


fruits = ['apple','banana','cherry']
fruits.pop(2)
print(fruits)

''' remove () : remves the item with the specified value.'''

fruits = ['apple','banana','cherry']
fruits.remove('banana')
print(fruits)


''' reverse() : reverse the order of the list .'''

fruits = ['apple','banana','cherry']
fruits.reverse()
print(fruits)

''' sort() : sort the given list.'''


cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)