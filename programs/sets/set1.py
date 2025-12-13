''' # 1.create a set with integers, strings, and floats, and display it.
set1 = {1, "Hello",4.0,False}
print(set1)

# 2. write s program if the given element exists in a set
set1 = {1,2,3,4,5,6}
element =  int(input("Enter an element:"))
if element in set1:
    print(f"{element} is in set")
else:
    print(f"{element} is not exist")

# using for loop
set1 = {1,2,3,4,5}
element = int(input("Enter an element :"))
found = False
for item in set1:
    if item == element:
        found = True
        break

if found:
    print(f" The {element} exist in a set")
else:
    print(f"The {element} is not exist in a set")

# using while loop
set1 = {1,2,3,4,5}
element = int(input("Enter an element"))
items = list(set1)  # converting set to list , since set has no indexing
found = False
i = 0
while i < len(items):
    if items[i] == element:
        found = True
        break
    i +=1
if found:
    print(f"The {element} is exist in a set")
else:
    print((f" The {element} is not exist"))

# 3.write a program to find the len of the set without using len() function

my_set = {1,2,3,4,5,6}
length = len(my_set)
print(length)

# without len() function
my_set = {1,2,3,4,5,6}
count = 0
for i in my_set:
    count +=1
print("The length of the set is:",count)

# using while loop
my_set = {1,2,3,4,5,6,7}
count = 0
items = list(my_set)
i = 0
while i < len(items):
    count +=1
    i += 1
print("The length is:",count)
# another way

my_set = {1,2,3,4,5}
s_list = list(my_set)
count = 0
i = 0
while s_list:
    s_list.pop()
    count +=1
    i +=1
print("Length :",count)

# using list comprehension
my_set = {1, 2, 3, 4, 5}
count = sum(1 for _ in my_set)
print("Length:", count)  # Output: 5

#4. write a program to add multiple elements to a set using add() and update() methods.

# add
my_set = {1,2,3,4,5}
elements = [6,7,8]
for element in elements:
    my_set.add(element)

print("The new set is :",my_set)

# update
my_set = {1,2,3,4,5}
elements = {6,7,8}
my_set.update(elements)
print(my_set)

# add single element and multiple elements by using both add , update method
my_set = {1,2,3,4,5}
single_element = 6
multiple_elements = (7,8,9)

my_set.add(single_element)
my_set.update(multiple_elements)

print(my_set)

my_set = {1,2,3,4,5}
elements = [6,7,8,2]
my_set.update(elements)
print(my_set)'''

# remove the elements from the set using remove(), discard(), and pop() the difference.

my_set = {1,2,3,4,5}
remove_element = my_set.remove(3)
print(my_set)   # remove method will remove the specified element,if the specified element does not exist in the
# given set , it raises a keyerror

my_set = {1,2,3,4,5}
remove_element = my_set.discard(3)
print(my_set)

# discard method wil remove the specified element, if the specified element does not exists , it returns nothing.

my_set = {1,2,3,4,5}
remove_element = my_set.pop()
print(my_set)
print(remove_element)    # it removes the random element from a set


# 6. write a program to clear the set
    # using clear()
my_set = {1,2,3,4,5}
result = my_set.clear()
print(my_set)

# 7. write a program to convert a list or tuple to a set (to remove duplicates)


# converting list to a set
my_list = [1,2,3,1,4,5,1]
l_set = set(my_list)
print(l_set)

# converting tuple to a set
my_tuple = (1,1,2,3,4,5,1)
t_set = set(my_tuple)
print(t_set)

# 9 iterate over through the set

my_set = {1,2,3,4,5,6}
for i in my_set:
    print(i)


def set_elements(s):
    for element in s:
        print(element)
my_set = {1,2,3,4,5}
set_elements(my_set)

# using while loop
def all_elements(s):
    for element in s:
        print(element)

my_set = {1,2,3,4,5}
all_elements(my_set)

# 8 create a frozen set and try modifying it (to understand immutability)
my_set = {1, 2, 3, 4, 5}
my_frozenset = frozenset(my_set)
print(my_frozenset)
print(type(my_frozenset))

my_list = [1,2,3,4,5]
my_frozenset = frozenset(my_list)
print(my_frozenset)
print(type(my_frozenset))

# creating empty frozenset
empty_frozenset = frozenset()
print(empty_frozenset)


# tried to remove an element from the frozenset, it raises an AttributeError: Frozenset object has no attribute 'add'

#my_frozenset = frozenset([1,2,4])
#my_frozenset.add(4)
#print(my_frozenset)

# 9.write a program to perform union operation between two sets
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)
print(set3)

   # using for loop
set1 = {1,2,3}
set2 = {4,5,6}
if set1 and set2:
    union_set = set1.union(set2)
else:
    print("one or both sets are empty")

print("Union:",union_set)

# using '|' operator

set1  = {1,2,3}
set2 = {4,5,6}
union_set = set1 | set2
print(union_set)

# 10.write a program to intersect two sets
set1 = {1,2,3,4}
set2 = {1,2,4,5}
set3 = set1.intersection(set2)
print(set3)

# using '&' (intersection) operator
set1 = {1,2,3,4}
set2 = {1,2,4,5}
set3 = set1 & set2
print(set3)

# using condition
set1 = {1,2,3,4}
set2 = {1,2,4,5}
if set1 and set2:
    intersection_set = set1.intersection(set2)
else:
    print("One or both sets are empty")

print("Intersection:",intersection_set)

# 11.write a program to perform difference operation
a = {1,2,3,4,5}  # the difference method will return the elements which are not in the another set
b = {1,2,3,6,7}
difference_set = a.difference(b)
print(difference_set)

# using '-' operator
a = {1,2,3,4,5}
b = {1,2,3,6,7}
difference_set = a - b

print(difference_set)

# using condition
a = {1,2,3,4,5}
b = {1,2,3,6,7}
if a and b:
    difference_set = a.difference(b)
else:
    print("one or both sets are empty")

print("Difference:",difference_set)

# 12. write a program to perform symmetric difference
a = {1,2,3,4,5}
b = {1,2,4,6,7}
symmetric_diff = a.symmetric_difference(b)    # the symmetric difference method will return the elements which are not in both sets
print(symmetric_diff)

# using '^' operator

a = {1,2,3,4,5}
b = {1,2,4,6,7}
symmetric_diff = a ^ b
print(symmetric_diff)
# using condition
a = {1,2,3,4,5}
b = {1,2,4,6,7}
if a and b:
    symmetric_diff = a.symmetric_difference(b)
else:
    print("one or both sets are empty")

print("Symmetric difference is:",symmetric_diff)


# 13. write  program to check if a set is subset or superset of another set

# issubset returns true if all the elements are present in another set, otherwise false

set1 = {1,2,3,4}
set2 = {1,2,3,4}
subset = set1.issubset(set2)
print(subset)

    # using  '< =' operator

set1 = {1,2,3,4}
set2 = {1,2,3,4}
subset = set1 <= set2
print("Subset:",subset)

# using condition
set1 = {1,2,3,4}
set2 = {1,2,3,4}
if set1 and set2:
    subset_set = set1  <= (set2)
else:
    print("One or both sets are empty")

print("The subset is:",subset_set)


# issuperset() : this method returns True if all elements of another set is present in this set
set1 = {1,2,3,4}
set2 = {1,2,3,4}
set3 = set1.issuperset(set2)
print(set3)


# using '<=' operator
set1 = {1,2,3}
set2 = {1,2,3}
set3 = set1 <= set2
print("The superset is:",set3)


# suing common elements
set1 = {1,2,3}
set2 = {1,2,3}
if set1 and set2:
    superset = set1.issuperset(set2)
else:
    print("One or other set is empty")
print("superset:",superset)



# 14. write a program to check if two sets are 'disjoint()' (no common elements)

# isdisjoint : Returns True if none of the elements are present in both sets, otherwise returns false
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = set1.isdisjoint(set2)
print("Disjoint:",set3)

# using condition
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
if set1 and set2:
    disjoint = set1.isdisjoint(set2)
else:
    print("One or other set is empty")

print("The disjoint is :",disjoint)

#15.find the common elements between three or more elements
set1 = {1,2,4,5}
set2 = {6,7,8,4}
set3 = {9,10,4,11}

common = set1.intersection(set2,set3)
print("Common element:",common)

# using '&' operator
set1 = {1,2,4,5}
set2 = {6,7,8,4}
set3 = {9,10,4,11}

common = set1 & set2 & set3
print("Common element is",common)


# using condition
set1 = {1,2,4,5}
set2 = {6,7,8,4}
set3 = {9,10,4,11}
if set1 and set1 and set2:
    common = set1.intersection(set2,set2)
else:
    print("one or another sets are empty")
print("The common element is:",common)

# using for loop
set1 = {1,2,4,5}
set2 = {6,7,8,4}
set3 = {9,10,4,11}

common = set()
for element in set1:
    if element in set2 and element in set3:
        common.add(element)
print(common)

# using while loop
set1 = {1,2,4,5}
set2 = {6,7,8,4}
set3 = {9,10,4,11}
common = set()
iterator = iter(set1)
while True:
    try:
        element = next(iterator)
        if element in set2 and element in set3:
            common.add(element)
    except StopIteration:
        break

print("common:",common)



list





