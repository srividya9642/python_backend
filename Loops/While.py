# While Loop
''' While loop in python is used to execute a block of statement repeatedly
 until the given condition is satisfied. When the condition becomes false
  the line immediately after the loop in the program is executed.'''

# Syntax ;
''' While test-execution:
        Body of while loop will be executed'''

count = 0

while(count <3):
 count = count+1
 print("Hello")




# Nested Loops:

''' Python programming allows us to use on loop inside another loop which is is called nested loop.'''


# Python Nested loops syntax :
#outer_loop expression :
  #Inner_loop expression:
    #Statement inside inner_loop
   #Statement inside Outer_loop


 # basic example of nested loops
x = [1,2]
y = [4,5]

for i in x :
   for j in y:
    print(i,j)

for i in range(1,5):
 for j in range(i):
     print(i, end = "")
 print()

''' In the above code we use nested loops to print the value of i multiple times
 in each row, where the number of times it prints i increase with each iteration of the outer loop.
 The print() function prints the value of i and moves to the next line after each row.'''


# printed multiplication table using python nested loop :


# running outer loop from 2 to 3
for i in range(2,4):

    # printing inside the outer loop
    # running inner loop from 1 to 10

    for j in range(1,11):

        # Printing inside the inner loop
        print(i, "%", j, "=", i*j)
    # printing inside the outer loop

    print()

for i in range(5,7):

    for j in range(1,11):
        print(i, "%", j, "=", i*j)

        print()

for i in range(2,4):
    for j in range(1,11):
        print(i, "%", j, "=", i*j)
        print()


# printing using different inner and outer nested loops

# Initialize list1 and list2
# with some strings
list1= ['Hello','good morning']
list2 = ['Hello','good afternoon']

# store length of list2 in list2_size
list2_size =len(list2)
# Running outer for loop to
# iterate though a list1.

# printing ouside inner loop
for item in list1:
    # printing outside inner loop
    print("Start outer for loop")
    i = 0
    # Running inner while loop to
    # iterate through a list2.

    while(i< list2_size):

        # printing inside inner loop
        print(item,list2[i])
        i = i+1    # incrementing the value of i

    print("end for loop")  # printing outside inner loop




# To reverse a string using for loop:

str = "Hello"
reversed_string = ""
i = len(str) - 1
while i>=0 :
    reversed_string += str[i]
    i-=1
print(reversed_string)



str = "Python"
reversed_string = ""
for i in str :
    reversed_string = i + reversed_string
    print(reversed_string)


for i in range(1,5):
    for j in range(i):
        print(i, end = "")
    print()


for i in range(2,4):
    for j in range(1,11):

        print(i,"%", j ,'=',i*j)
    print()
