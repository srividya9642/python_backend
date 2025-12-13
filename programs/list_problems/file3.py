'''# 17. write a program to sort the list (ascending and descending) without using sort method.
my_list = [1,4,3,6,5,2,7,8,10,9]
my_list.sort()
print("Ascending order:",my_list)

# descending order
my_list = [1,4,3,6,5,2,7,8,10,9]
my_list.sort(reverse=True)
print("Descending order:",my_list)

my_list = [1,4,3,6,5,2,7,8,10,9]
ascending_list = sorted(my_list)
print(ascending_list)
        
my_list = [1,4,3,6,5,2,7,8,10,9]
descending_list =sorted(my_list,reverse=True)
print(descending_list)

    # using a simple loop with comarision(like insertion logic)
numbers = [1,4,3,6,5,2,7,8,10,9]
asc = []


for num in numbers:
    inserted = False
    for i in range(len(asc)):
        if num < asc[i]:
            asc.insert(i, num)
            inserted = True
            break
    if not inserted:
        asc.append(num)
        
               
print("Ascending:", asc)

# descending
my_list = [1,4,3,6,5,2,7,8,10,9]
desc = []

for num in my_list:
    inserted = False
    for i in range(len(desc)):
        if num > desc[i]:
            desc.insert(i,num)
            inserted = True
            break
    if not inserted:
            desc.append(num)
            
print("Descending:",desc)


#18. write a program to multiply all elements in a list.

my_list = [1,2,3,4,5,6,7,8,9,10]
result = 1
for num in my_list:
    result *= num
    
print("The product of list is :",result)

# using math.prod() function


import math
my_list = [1,2,3,4,5]
product = math.prod(my_list)

print("The product of the list is:",product)

# write a progrsm to separate negative and positive values from a list

my_list = [1,-2,3,-4,5,-6,7,-8]
negative_num = 0
positive_num = 0
for num in my_list:
    if num >0:
        positive_num +=1
    elif num< 0:
        negative_num +=1
        
print("Positive nums:",positive_num)
print("Negative list:",negative_num)


# using list comprehension
my_list = [1,-2,3,-4,5,-6,7,-8]

positive_num = [x for x in my_list if x>0]
negative_num = [x for x in my_list if x<0]

print("postive:",positive_num)
print("Negative:",negative_num)


# using while loop
my_list = [1,-2,3,-4,5,-6,7,-8]
positive = []
negative = []
i = 0

while i < len(my_list):
     if my_list[i] > 0:
        positive.append(my_list[i])
     elif my_list[i] < 0:
         negative.append(my_list[i])
     i +=1
    
    
print("Positive numbers:",positive)
print('Negative numbers:',negative)
         
         
# 18 write a program to find the largest and smallest numbers in a list with one loop

my_list = [1,2,3,4,5]
largest = smallest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
        
print("The largest:",largest)
print("The smallest:",smallest)


# using list built-in method
my_list = [1,2,3,4,5]
result = [my_list[0], my_list[0]]

for num in my_list:
    result[0] = max(result[0],num)
    result[1] = min(result[1], num)
    
print("Largest number:",result[0])
print("Smallest number:",result[1])
        
        
# 19. wrtite a program to peint all unique elements in a list
my_list = [1,2,1,3,4,1,2,3,5]
unique = []
for num in my_list:
    if num not in unique:
        unique.append(num)
   
        
print("The unique nums is:",unique)

# using set()

my_list = [1,2,1,3,4,1,2,3,5]

unique = list(set(my_list))
print(unique)        


# using dictionary

my_list = [1,2,1,3,4,1,2,3,5]

unique = list(dict.fromkeys(my_list))
print(unique)
    
    
# using list comprehension

my_list = [1,2,1,3,4,1,2,3,5]
unique = [x for x in my_list if my_list.count(x) == 1]
print("Unique elements:",unique)


# using while loop
my_list = [1,2,1,3,4,1,2,3,5]
unique = []
i = 0
while i < len(my_list):
    if my_list[i] not in unique:
        unique.append(my_list[i])
        i +=1
print("Unique elements:",unique)  

# 21. write a progrsm to find the frequency of each element in a list using dictionary
my_list = [1,2,1,2,3,4,5,5,6]
freq = {}
for num in my_list:
    if num  in freq:
        freq[num] +=1 
    else:
        freq[num] = 1
        
print("The frequency of the nums is:",freq)   


# using while loop:
my_list = [1,2,1,2,3,4,5,5,6]
freq = {}
i = 0
while i < len(my_list):
    num = my_list[i]
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1
    i +=1
    
print("The freq is:",freq)


# 22. write a program to merge two lists into a single sorted list
list1 = [1,3,2,5,4,6]
list2 = [7,8,10,11,12,13]
merged = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i +=1
    else:
        merged.append(list2[j])
        j +=1
        
merged.extend(list1[i:])
merged.extend(list2[j:])


print("Merged sorted list:",merged)


# using + and sorted()
list1 = [1,3,5,7]
list2 = [2,4,6,8]

merged = sorted(list1 + list2)
print("Merged sorted list:",merged)

list1 = [1,3,5,7]
list2 = [2,4,6,8]
merged = []

while list1 and list2:
    if list1[0] < list2[0]:
        merged.append(list1.pop(0))
    else:
        merged.append(list2.pop(0))
        
        
merged.extend(list1)
merged.extend(list2)


print("Merged sorted list:",merged)

# using set union method

list1 = [1,3,5,7]
list2 = [2,4,6,8]
merged = list(set(list1) | set(list2))
print("The unique merged sorted list is:",merged)


# 23 write a progrsm to flatten a list

#my_list = [[1,2,[3]],4]
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
            
    return flat

nested = [[1,2,[3]],4]
print("Flatten List:",flatten_list(nested))

# using while loop and type checking

nested = [[1,2,[3],[4]]]
flat = []
while nested:
    item = nested.pop(0)
    if isinstance(item, list):
        nested = item + nested
    else:
        flat.append
        
print("The flattend list is :",nested)'''

#24. write a program to check if two lists are equal(same elements and same order)

list1 = [1,2,3]
list2 = [1,2,3]

if list1 == list2:
    print("Lists are equal")
else:
    print("Lists are not eual")
    
# using for loop (manual comparision)
list1 = [1,2,3]
list2 = [1,2,3]

if len(list1) != len(list2):
    print("Lists are not eual")
else:
    eual = True
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            equal = False
            break
        
    if equal:
        print("Lists are equal")
        
    else:
         print("Lists are not equal")
         
# using while loop
list1 = [1,2,3]
list2 = [1,2,3]
i = 0
equal = True
if len(list1) == len(list2):
    while i < len(list1):
        if list1[i] != list2[i]:
            equal = False
        i +=1
else:
    equal = False
    
if equal:
    print("Lists are equal")
else:
    print("Lists are not equal")
    
# 25. write a progrsm to rotate a list by k elements
my_list = [1,2,3,4,5]
k = 2
for i in range(k):
    last = my_list.pop()
    my_list.insert(0,last)
    
print("Rotated List:",my_list)

# using while loop
my_list = [1,2,3,4,5]
k = 2
i = 0
while i < k:
    first = my_list.pop()
    my_list.insert(0,first)
    i +=1
    
print("Rotated List:",my_list)