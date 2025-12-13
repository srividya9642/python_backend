# Nested Loops
''' Python programming language allows to use one loop inside another lopp which is called "Nested Loop"'''

for i in range(1,5):
    for j in range(i):
        print(i , end = "")
    print()

# example 2

for i in range(2):
    print(i)
    for j in range(10,13):
        print(j)


# basic example of python nested loops

x = [1,2]
y = [4,5]
for i in x :
    for j in y :
        print(i,j)

#2

x = [1,2]
y = [4,5]
i = 0
while i < len(x) :
    j = 0
    while j < len(y) :
        print(x[i], y[j])
        j = j+1
    i = i+1


# printing using different inner and outer nested loops :

# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

# Store length of list2 in list2_size
list2_size = len(list2)

# Running outer for loop to
# iterate through a list1.
for item in list1:

    # Printing outside inner loop
    print("start outer for loop ")
    # Initialize counter i with 0
    i = 0
    # Running inner While loop to
    # iterate through a list2.
    while(i < list2_size):

        # Printing inside inner loop
        print(item, list2[i])
        # Incrementing the value of i
        i = i+1
    # Printing outside inner loop
    print("end for loop ")




# Using break statement in nested loop
for i in range(2,4):
    for j in range(1,11):
        if i==j:
            break
        print(i,'*', j, '=', i*j)
    print()


# Using continue statement in nested loops ;

for i in range(2,4):
    for j in range(1,11):
        if i==j:
            continue
        print(i,"*",j, '=', i*j)
    print()

