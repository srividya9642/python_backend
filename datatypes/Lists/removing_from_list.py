# we can remove elements from a list using :

# remove() :  Removes the first occurence of an element.
# pop()    : Removes the element at a specific index or the last element if no index is specified.
# del statement() : deletes an element at a specified index.



a = [10,20,30,40,50]
a.remove(30)
print("After remove(30):", a)

popped_value = a.pop(1)
print("popped element:", a)
print("After pop(1):",a)

a = [10,20,30,40,50]
del a[0]
print("After del:", a)