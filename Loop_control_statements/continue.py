# continue statement:
''' pythone continue statement is a loop control statement that forces to executes the next iteration
of the loop while skipping the rest of the code inside the loop for the current iteration only.
i,e. when the continue statement is executed in the loop, the code inside the following the continue statement will
be skipped for the current iteration andthe next ieration of the loop will begin.'''

# syntax :
while True:
        if x == 10:
            continue
        print(x)


# example :

for i in range(5):
    if i == 3:
        continue   # skip the ret of the code for i = 3
    
    print(i)


# ex 2
for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")
    
    
# Examples of continue statements
#1 Skipping specific characters in a string

for char in "Welcome":
    if char == "e":
        continue
    print(char, end=" ")
    
    
#2 using continue in  nested loops.

a = [[1,2,3],[4,5,6],[7,8,9]]
for row in a :
    for num in row:
        if num == 3 :
            continue
        print(num, end = " ")
        

#3 using continue with a wjile loop.

i = 0
while i < 10 :
    if i == 5 :
        i += 1 # ensure that loop variable is incremented to avoid infinite loop
        continue
    print(i)
    i +=1