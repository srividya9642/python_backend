# 1. write a program to calculate the sum of the all elements in a list.
my_list = [1,2,3,4,5]
total = sum(my_list)
print(total)

# using for loop.....
my_list = [1,2,3,4,5]
total = 0
for ch in my_list:
    total += ch
print("The sum is:",total)

# using while loop.....
my_list = [12,20,30,40,50]
total = 0
i = 0
while i <len(my_list):
    total +=my_list[i]
    i +=1
    
print("The total sum is:",total)

# using recursive function

def list_sum(lst):
    if not lst:
        return  0
    return lst[0] + list_sum(lst[1:])

my_list = [10,20,30,40,50] 
print("Sum is:",list_sum(my_list))

# Uisng list comprehension

my_list = [1,2,3,4,5]
total = sum([x for x in my_list])
print('The sum of the list is :',total)



# 2. write a program to Find the maximum and minimum elements in a list
my_list = [1,2,3,4,5]
maximum = max(my_list)
minimum = min(my_list)

print("The maximum number is:",maximum)
print("The minimum number is:",minimum)


# using for loop..
my_list = [1,2,3,4,5]
maximum = my_list[0]
minimum = my_list[0]
for num in my_list:
    if num > maximum:
        maximum = num
    if num < minimum:
       minimum = num
        
print('The maximum number is:',maximum)
print("The minimum number is:",minimum)

# using the sorted method
my_list = [1,2,3,4,5]
sorted_list = sorted(my_list)
maximum = sorted_list[0]
minimum = sorted_list[-1]

print("Maximum:",maximum)
print("Minimum:",minimum)
 
# 3.write a programs to find the number of occurraences of a spefied element in a list
 
my_list = [1,2,2,3,1,4,5]   # using built-in methods
element = int(input("Enter a number:"))
occurrences = my_list.count(element)
print(occurrences)


# uisng for loop
my_list = [1,2,1,2,2,4,5]
element = int(input("enter an element:"))
count = 0
for num in my_list:
    if num == element:
     count +=1
     
print(count)


# using while loop

my_list = [1,2,1,3,4,5,2]
element = int(input("Enter an element"))
count = 0
i = 0
while i <len(my_list):
   if my_list[i] == element:
      count +=1
   i +=1
    
print(count)

# using list comprehension

my_list = [1, 2, 3, 1, 2, 1, 4, 5]
element = int(input("Enter an element:"))
occurrences = len([item for item in my_list if item == element])
print(occurrences)

#4. Write a program to reverse a list
my_list = ["apple","banana","cherry"]
reversed_iterable = reversed(my_list)
reversed_list = list(reversed_iterable)

print("Reversed list is:",reversed_iterable)

# Using slicing
my_list = ["apple","banana","cherry"]
reversed_list = my_list[::-1]
print(reversed_list)

# using for loop
my_list = ['apple','banana','cherry']
reversed_list = []  # initializes an empty list to hold the reersed elements.


# This for loop iterates over the indices of my_list starting from the last index(len(my_list) -1, which is 4) to 0, decrementing by 1
# each time (that's what the -1 step means).
for i in range(len(my_list)-1, -1, -1): 
    reversed_list.append(my_list[i])
print(reversed_list)

# // uisng list comprehension
my_list = ['apple','banana','cherry']
reversed_list =[my_list[i] for i in range(len(my_list)-1,-1,-1)]
print(reversed_list)

# // using a loop with insert at position 0
my_list = ['apple','banana','cherry']
reversed_list = []
for item in my_list:
    reversed_list.insert(0,item)
    print(reversed_list)
    
    
# 5. write a program to find the length of the string without using length function
my_list = [10,20,30,40,50,6,4,11]
count = 0
for ch in my_list:
     count +=1
    
    
print("Length of the string is:",count)

# using while loop
my_list = [10,20,30,40,11,22,3,4,8]
count = 0
i = 0
while True:
    try:
        my_list[i]
        count += 1
        i  +=1
    except IndexError:
        break
    
print("Length of the list:",count)

# using list comprehension

my_list = [10,20,30,40,12,11,45]
length = sum(1 for i in my_list)
print("Length of the list:",length)


# 6. write a program to check if an element exists in a list or not

my_list =[1,2,3,4,5,11,56]
element = int(input("Enter an element"))
exists = element in my_list
print(exists)

# using for loop
my_list = [10,20,30,23,12,11,98]
element = int(input("Enter the element"))
found = False
for item in my_list:
    if item == element:
        found = True
        break
print(found)

# using count method
my_list = [11,20,20,23,44,545,55]
element = int(input("Enter an element"))
exists = my_list.count(element) > 0
print(exists)

# using list comprehension

my_list = [10,20,30,40,50]
element = int(input("Enter an element:"))
exists = any(item == element for item in my_list)
print(exists)


        

    