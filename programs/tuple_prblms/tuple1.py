# 1. create an empty tuple
t = ()
print(t)
print(type(t))

  # using tuple constructor
t = tuple()
print(t)
print(type(t))


# 2. create a tuple with integers
t = (1,2,3,4,5,6)
print(t)
   # using tuple constructor
t= tuple((1,2,3,4,5))
print(t)


# 3.creata a tuple with different data types
t = (1,2,3.5,"hello",True)
print(t)

# 4. Access the first and last middle elements of a tuple
t = (1,2,3,4,5)
index = t[0:6:1]
print(index)

# using while loop
i = 0
length = len(my_tuple)

while i < length:
    if i == 0:
        first = my_tuple[i]
    if i == length - 1:
        last = my_tuple[i]
    if i == length // 2:
        middle = my_tuple[i]
    i += 1

print("First:", first)
print("Last:", last)
print("Middle:", middle)

# 5.convert a list in to tuple
lst = [1,2,3,4,5]
t = tuple(lst)
print(t)
print(type(t))

# 6. convert a tuple into a list
t = (1,2,3,4,5)
lst = list(t)
print(lst)
print(type(lst))

# 7. find the length of a tuple.
t = (1,2,3,4,5)
length = len(t)
print(length)

# using count
t = (1,2,3,4,5)
count = 0
for num in t:
    count +=1
    
print("The length is:",count)

# using enumarate
t = (1,2,3,4,5)
length = 0
for i,_ in enumerate(t,1):
    length = i
    
print(length)

# 8. check if a specific element exists in a tuple
my_tuple = (1, 2, 3, 4, 5)
element = 1

if element in my_tuple:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")
    
#   using while loop

my_tuple = (1,2,3,4,5)
element = 6
found = False
i = 0
while  i < len(my_tuple):
    if my_tuple[i] == element:
        found = True
        break
    i +=1
if found:
    print("element exists in the tuple.")
else:
    print("element does not exists in the tuple.")      

# 10. write a program to count the occurences of a specified element in a tuple

my_tuple = (1, 2, 3, 2, 4, 2, 5)
count = 0
element = int(input(("Enter an element: ")))
for item in my_tuple:
    if item == element:
        count += 1
print(count)

# using while loop
my_tuple = (1,2,1,3,4,5,1)
element = int(input("Enter an element:"))
count = 0
i = 0
while i < len(my_tuple):
    if my_tuple[i] == element:
        count +=1
    i +=1

print("The element count is:",count)

# 11. write a program to contate two tuples

   # using '+' operator
t1 = (1,3,5,7)
t2 = (2,4,6,8)
concate = t1 + t2
print(concate)

   # using sum() function with a tuple of tuples
t1 = (1,3,5,7)
t2 = (2,4,6,8)
result = sum((t1, t2),())
print("Concatenated tuple:",result)
    # using for loop

t1 = (1,3,5,7)
t2 = (2,4,6,8)
result = ()
for num in t1:
    result +=(num,)
for num in t2:
    result +=(num,)


# using while loop
t1 = (1,3,5,7)
t2 = (2,4,6,8)
result = ()
print("Concatenated tuple is:",result)

# using tuple list conversion
t1 = (1,3,5,7)
t2 = (2,4,6,8)
result = tuple(list(t1) + list(t2))
print("Concatenated Tuple:", result)

# using unpacking (* operator)
t1 = (1,3,5,7)
t2 = (2,4,6,8)
result = (*t1, *t1)

print(result)

# 12 write a program to repeat a tuple multiple times
my_tuple = (1,2,3,4)
repeated = my_tuple * 3
print(repeated)

    # using for loop
my_tuple = (1,2,3)
n = 3
result = ()
for i in range(n):
    result += my_tuple
print(result)

# using list conversion
t = (5,10)
n = 4
repeated = tuple(list(t) * n)
print(repeated)


# using List comprehension & tuple()
t = (1,2,3)
n = 2
repeated = tuple(item for i in range(n) for item in t)
print(repeated)

# slice the tuple( eg. first 3 elements, last 2 elements, every second element)
my_tuple = (1,2,3,4,5,6,7,8)
result = my_tuple[:3]
result2 = my_tuple[-2:]
result3 = my_tuple[::2]
print(result)
print(result2)
print(result3)

# using slice function
first_three = my_tuple[slice(0,3)]
last_two = my_tuple[slice(-2,None)]
every_second = my_tuple[slice(0,None, 2)]

print("First 3:",first_three)
print("Last 2:",last_two)
print("Every second:",every_second)

# using for loop (manual slicing)

my_tuple = (1,2,3,4,5)
first_three = ()
for i in range(3):
    first_three += (my_tuple[i],)
last_two = ()
for i in range(len(my_tuple) -2, len(my_tuple)):
    last_two += (my_tuple[i],)
every_second = ()
for i in range(0, len(my_tuple), 2):
    every_second += (my_tuple[i],)


print("First 3:",first_three)
print("Last two:",last_two)
print("Everysecond:",every_second)

# 14, find the maximum and minimum value in a numeric element
my_tuple = (1,2,3,4,5)
maximum = max(my_tuple)
minimum = min(my_tuple)

print("Maximum:",maximum)
print("Minimum:",minimum)

# using sorted method
my_tuple = (1,2,3,4,5)
sorted_list = sorted(my_tuple)
maximum = sorted_list[-1]
minimum = sorted_list[0]
print(maximum)
print(minimum)

# using sort method
my_tuple = (1,2,3,4,5)
maximum = my_tuple[0]
minimum = my_tuple[0]
for num in my_tuple:
    if num > maximum:
     maximum = num
    elif num < minimum:
       minimum = num

print("Maximum:",maximum)
print("Minimum:",minimum)

# using while loop:
my_tuple = (1,2,3,4,5)
maximum = my_tuple[0]
minimum = my_tuple[0]
i = 0
while i < len(my_tuple):
    if my_tuple[i] > maximum:
        maximum = my_tuple[i]
    if my_tuple[i] < minimum:
        minimum = my_tuple[i]
    i +=1

print(maximum)
print(minimum)

# using tuple comprehension
my_tuple = (1,2,3,4,5)
maximum = (x for x in my_tuple if x>my_tuple[i])
minimum = (x for x in my_tuple if x < my_tuple[i])

print(maximum)
print(minimum)

# 15. calculate sum of all elements in a numeric tuple.
my_tuple = (1,2,3,4,5)
total = sum(my_tuple)
print(total)

# using tuple comprehension
my_tuple =(1,2,3,4,5)
total = sum(x for x in my_tuple)
print("sum is:",total)

# using for loop
my_tuple = (1,2,3,4,5)
total = 0 
for num in my_tuple:
    total = total + num

print("the sum of the tuple is:",total)

# using while loop:
my_tuple = (1,2,3,4,5)
total = 0
i = 0
while i < len(my_tuple):
    total += my_tuple[i]
    i +=1
print("The sum :",total)

# 16. find the product of all element in a numeric tuple

my_tuple = (1,2,3,4,5)
product = 1
for num in my_tuple:
    product *= num
print("The product of elements is:",product)

# using while loop
my_tuple = (1,2,3,4,5)
product = 1
i = 0
while i < len(my_tuple):
    product *= my_tuple[i]
    i +=1
print(product)

# 17. Reverse a tuple
my_tuple = (1,2,3,4,5)
rev = ()
for i in range(len(my_tuple)-1, -1, -1):
    rev += (my_tuple[i],)

print("The reversed tuple is:",rev)

# using while loop
t = (1, 2, 3, 4, 5)
reversed_t = ()
i = len(t) - 1
while i >= 0:
    reversed_t += (t[i],)
    i -= 1
print(reversed_t)  # Output: (5, 4, 3, 2, 1)

# using list slicing
my_tuple = (1,2,3,4,5)
rev = my_tuple[::-1]
print(rev)


# 18. sort a tuple pf numbers
my_tuple = (1,3,4,5,2,6)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)
# using sort method
my_tuple = (1,3,4,5,2,6)
t_list = list(my_tuple)
t_list.sort()
sorted_tuple = tuple(t_list)
print(sorted_tuple)


# using for loop
my_tuple = (1,3,4,5,2,6)
t_list = list(my_tuple)
for i in range(len(t_list)):
    for j in range(len(t_list) - 1):
        if t_list[j] > t_list[j + 1]:
            t_list[j], t_list[j + 1] = t_list[j + 1], t_list[j]


sorted_t = tuple(t_list)
print(sorted_t)

# using while loop
my_tuple = (1,3,4,2,6,5)
t_list = list(my_tuple)
n = len(t_list)
i = 0
while i < n:
    j = 0
    while j < n - 1:
        if t_list[j] > t_list[j + 1]:
            t_list[j], t_list[j + 1] = t_list[j + 1], t_list[j]
            j += 1
        i += 1
sorted_t = tuple(t_list)
print(sorted_t)

# 19. sort a list alphabetically
my_tuple = ("apple","watermelon","grapes","banana","cherry")
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)

# using sort method
my_tuple = ("apple","watermelon","grapes","banana","cherry")
t_list = list(my_tuple)
sorted_tuple = tuple(t_list)
print(sorted_tuple)

# using for loop
my_tuple = ("apple","watermelon","grapes","banana","cherry")
t_list = list(my_tuple)

for i in range(len(t_list)):
    for j in range(len(t_list) - 1):
        if t_list[j] > t_list[j + 1]:
            t_list[j], t_list[j + 1] = t_list[j + 1], t_list[j]

sorted_t = tuple(t_list)
print(sorted_t)







