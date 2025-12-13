# List is a ordered sequence of items.
# it is one of the most used and flexible data type.
# creating a list is pretty simple, to create a list we can insert the items sepated by come and within the square brackets.
# The indes is starts from "0" in python by default.
# List is mutable which means, elements can be altered into list.


# Crearting a list :
l = []
print(type(l))




# Access elements from a list:  there are various ways to access the elements from a list

# 1. using list index : We can use list index to access the elements within a list.
# The index must be an integer only, we cant't use float,or other data types. This will result the type error


l = [1,2,3,4,5]
print(l[1])



# Negative indexing :
'''Negative indexing starts from the end "-1" : refers the last value, -2 : refers the last second value.'''

# example :   print the last item from a list

l = [10,20,30,40,50]
print(l[-1])

# Range of indexes : 
''' We can specify a range of index where to start and where to end the range.
when speifying a range, the return value will be a new list with the specified items.'''

# Ex : return the 3,4,and 5 values in a list

l = [1,2,3,4,5,6,7]
print(l[3:6])

l = ["apple", "banana","orange","watermelon","grapes"]
print(l[2:5])

# Range of negative indexes :

''' Specofy negative indexes if we want to start the searc from the end of the list.'''
# Ex : this ex returns the item from "orange(-4)" but not include "mango(-1)"

list1 = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(list1[-4:-1])


# Check if the item exists :
''' to determine if a specified item is present in a list, we can use 'in' keyword.'''


l = [ "apple","orange","banana","mango"]
if "mango" in l:
    print("yes!, apple is in list")
    
    
    
# Change item value : To chane the value of a specific item, refer to the index number.

# ex : change the second item :
l1 = ["apple","banana","cherry"]
l1[1] = "blackberry"
print(l1)


# List constructor :  we can also create a list by passing an iterable (like a tuple,string or another list) to the list() function.

a = list((1,2,3, 'apple',4.5))
print(a)

b = list("GM")
print(b)





# Creating a list with repeated elements: We can use the multiplication operator * to create a list with repeated items.

a = [2] * 5
b = [0] * 7

print(a)
print(b)






# iterating over a list:

''' We can iterate over lists using "loops". which is useful for performing actions on each item.'''


a = ["apple","banana","orange"]
for item in a :
    print(item)
    
    
# Nested lists ;
''' A nested list is a list within another list, which is useful for representing matrices or tables. we can access nested elements by chaining indexes.'''
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])



# ex2 :

l =[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in l:
     print(j)



