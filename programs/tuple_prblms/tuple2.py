'''# 20 write a progrm to check whether two tuples are equal
t1 = (1,2,3,4,5)
t2 = (1,2,3,4,5)
t3 = (t1 == t2)
print(t3)
print("Yes the two tuples are equal")


# using for loop
t1 = (1,2,3,4,5)
t2 = (1,2,3,4,5)
are_equal = True
if len(t1) != len(t2):
    are_equal = False
else :
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            are_equal = False
            break
print(f"The both tuples are {are_equal}")

# using while loop
t1 = (1,2,3,4,5)
t2 = (1,2,3,4,5)
equal = True
if len(t1) != len(t2):
    equal = False
else:
    while i < len(t1):
        if t1[i] != t2[i]:
            equal = False
            break
print(f'The two tuples are {equal}')'''

# 21 create a nested tuples and access the elements from it
my_tuple = (10,20,(30,40,50),60)
print(my_tuple[1][2])


