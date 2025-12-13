# 16. Given two lists find the common elements using sets
list1 = [1,2,4,5,6]
list2 = [7,6,9,10,4]

set1 = set(list1)
set2 = set(list2)
if set1 and set2:
    common = set1.intersection(set2)
else:
    print("One or another set is empty")
print("The common elements are :",common)

# using '&' operator

list1 = [1,2,4,5,6]
list2 = [7,6,9,10,4]

set1 = set(list1)
set2 = set(list2)
common = set1 & set2

print("THe common elements are:",common)


# 17 remove all elements from one set that are present in another(difference update).

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
s1.difference_update(s2)
# s1 is now {1, 2, 3}
print(s1)

# using -= operator
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
set1 -= set2
print(set1)

# 18. Copy one set to another and verify that modifying one doesn’t affect the other.

set1 = {1,2,3,4,5,6}
set_copy = set1.copy()
set_copy.add(7)
print(set1)
print(set_copy) # modifying copied set doesn't change original set

# using set constructor
set1 = {1,2,3,4,5}
new_set = set((1,2,3,4,5))
new_set.add(6)
print(new_set)
print(set1)

# using set constructor
set1 = {1,2,3,4,5}
copied_set = {x for x in set1}
print(copied_set)

#21 Find the unique elements from two lists using sets.

list1 = [1,2,3,4,5,6]
list2 = [1,2,3,7,8,9]

unique_elements =list(set(list1) ^ set(list2))

print(unique_elements)
# the '^' or symmetric_difference() returns elements that are in either of the
# sets but not in both. This is perfect for finding unique elements across two lists.



# using set union and intersection

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7,8]
unique_elements = list((set(list1) | set(list2)) - (set(list1) & set(list2)))
print(unique_elements)


# 22. find the duplicate elements in a list using sets.





