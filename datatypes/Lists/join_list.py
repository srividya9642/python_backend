# There are several way to join, or concatinate, two or more lists in python.
# one of the most easiest ways are by using '+' operator.abs




# join two  lists ;
list1 = ['a','b','c']
list2 = [1,2,3]

list3 = list1+list2
print(list3)


# Another way to join two lists by appending all the items from  list2 into list1, one by one :

list1 = ['a','b','c']
list2 = [1,2,3]
for x in list2 :
    list1.append(x)
    
print(list1)



# or we can use extend() method. where the purpose is to add elements from one list to another list :


list1 = ['a','b','c']
list2 =[1,2,3]

list1.extend(list2)
print(list1)