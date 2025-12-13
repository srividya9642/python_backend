# 7. write a progrsm to remove duplicates from a list

my_list = [10,20,10,30,40,50]
new_list = list(set(my_list))
print(new_list)

my_list = [1,1,2,3,2,4,5,5]
new_list = []
for ch in my_list:
    if ch not in new_list:
        new_list.append(ch)
print(new_list)

# using while loop
my_list = [1,2,3,1,3,4,5]
new_list = []
i = 0
while i < len(my_list):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
    i +=1
print("The string without duplicates:",new_list)

# using list comprehension

a = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique_list = [x for x in a if not (x in seen or seen.add(x))]
print(unique_list)  # Output: [1, 2, 3, 4, 5]

# using function
def remove_duplicates(lst):
    new_list = []
    for val in lst:
        if val not in new_list:
            new_list.append(val)
    return new_list
            
            
my_list = [1,1,2,3,2,3,4,5]
result = remove_duplicates(my_list)
print("the list without duplicates:",result)


# while loop
def remove_duplicates(lst):
    unique = []
    i = 0
    while i < len(lst):
        if lst[i] not in unique:
            unique.append(lst[i])
        i += 1
    return unique

my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print("List after removing duplicates:", result)

# 8.write a program to get the index of a specific element in a list
my_list = [1,2,2,3,4,5,6]
element = int(input("Enter an element"))
index = my_list.index(element)
print(index)


# using for loop with enumaration
my_list = ["apple","banana","cherry","grapes","papaya","watermelon"]
element = input("Enter an element:")
for idx,val in enumerate(my_list):
    
# enumarate(my_list) returns an iterator of pairs :(index, value) for each element in the list.
    if val == element:
        print(idx)
        break
    
    
# using list comprehension
my_list = [1,2,3,4,5,6]
element = int(input("Enter an element:"))
index = [ i for i, x in enumerate(my_list) if x == element]
print(index)

# 9. write a progrsm to return a copy of the list without using copy() method

my_list = [1,2,3,4,5,6]
new_list = []
for item in my_list:
    new_list.append(item)
print(new_list)

# using list slicing

my_list = [1,2,3,4,5,6]
new_list = my_list[:]
print(new_list)

# using list constructor
my_list = [1,2,3,4,5,6]
new_list = list(my_list)
print(new_list)

# using list comprehension
my_list = [1,2,3,4,5,6,7]
new_list = [item for item in my_list]
print(new_list)

# using while loop
my_list = [1,2,3,4,5,6]
new_list = []
i = 0
while i<len(my_list):
    new_list.append(my_list[i])
    i +=1
print(new_list)

# 10 write a program to remove all even numbers from a list

       # using for loop
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in my_list:
    if i%2 !=0:
        new_list.append(i)
print(new_list)

    # using while loop
my_list = [1,2,3,4,5,6,7,8,9,10]

i = 0
while i <len(my_list):
    if my_list[i] %2 == 0:
        my_list.pop(i)
    else:
        i +=1
print(my_list)

     # using list comprehension
     
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = [num for num in my_list if num %2 !=0]
print(new_list)

# 11. write a program to find the second largest number in a list
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.sort()
print('Second largest num:',my_list[-2])

      # using sorted method
my_list = [1,2,3,4,5,6,7,8,9,10]
second_large = sorted(my_list)[-2]
print(second_large)

    # using manual comparision
my_list = [10,20,30,40,50,60]
first = second = float('-inf')
for num in my_list:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second largest number:",second)

# without using sort by removing max()
my_list = [10,20,30,40,50,60]
max_num = max(my_list)
my_list.remove(max_num)
second_largest = max(my_list)
print("Second largest :",second_largest)

    
    
# 12.write s program to find second smallest number in a list
my_list = [11,43,29,32,27,78,22]
my_list.sort()
print(my_list[1])

# using sorted method
my_list = [11,43,29,32,27,78,22]
second_smallest = sorted(my_list)[1]
print("Second smallest:",smallest)

# without using sort method nd removing min()
my_list = [11,43,29,32,27,78,22]
min_num = min(my_list)
my_list.remove(min_num)
second_smallest = min(my_list)
print("The second smallest is:",second_smallest)

# using a for loop (manual comparision)
my_list = [11,43,29,32,27,78,22]
first = second = float('inf')
for num in my_list:
    if num < first:
        second = first
        first = num
    elif num < second and num != first:
        second = num
print("Second smallest is:", second)


      # using function
def second_smallest(numbers):
    first = second = float('inf')
    for num in numbers:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
            
            
    return second
            
my_list = [11,43,29,32,27,78,22]
print("Second smallest:",second_smallest(my_list))

# 13. Write a program to find common elements in two lists.
      
          # by using set intersection(&)

list1 = [10,20,30,40,50]
list2 = [60,70,80,10,40]
commom_elements = list(set(list1) & set(list2))
print(commom_elements)


    # by using for loop
list1 = [1,2,3,4,5,6]
list2 = [4,5,7,8,9]
new_list = []
for ch in list1:
    if ch in list2:
        new_list.append(ch)
        
print("Common elements are:",new_list)


 # 14. write a program to find elements present in one list but not in another.

      # Using for loop

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,1,2,3]
new_list = []
for ch in list1:
    if ch not in list2:
        new_list.append(ch)
        
print("The elements not present in another list:",new_list)

      # using list comprehension
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,1,2,3]
new_list = [x for x in list1 if x not in list2]
print(new_list)

        # using set difference operator(-)
        
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,1,2,3]
new_list = list(set(list1) - set(list2))
print("The list is:",new_list)

     # using while loop
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,1,2,3]
new_list = []
i = 0
while i<len(list1):
    if i not in list2:
        new_list.append(i)
        i +=1
print("The list is:",new_list)
        
        
        
# 15. write a program to count the number of even and odd numbers from a list
       
       # using for loop
       
my_list = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
odd_count = 0
for i in my_list:
    if i%2 ==0:
        even_count +=1
    else:
        odd_count +=1
        
print("Even count is:",even_count)
print("Odd_count:",odd_count)


  # using list comprehension
my_list = [1,2,3,4,5,6,7,8,9,10]
even_count = [x for x in my_list if x%2 ==0]
odd_count = [x for x in my_list  if x%2 !=0]
print("The even count:",even_count)
print("The odd count:",odd_count)

# using while loop
my_list = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
odd_count = 0
i = 0
while i <len(my_list):
    if my_list[i]%2 == 0:
        even_count +=1
    else:
        odd_count +=1
    i +=1
print("The even count is:",even_count)
print("The odd count is:",odd_count)

# using sum with boolean logic
my_list = [1,2,3,4,5,6,7,8,9,10]
even_count = sum(num %2 == 0 for num in my_list)
odd_count = sum(num %2 !=0 for num in my_list)

print("Even count:",even_count)
print("Odd count:",odd_count)

















    
    
