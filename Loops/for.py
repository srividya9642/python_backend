# Loops in python :

''' loops in python are used to repeat actions efficiently.
 The main types are For loops(counting through items) and While loops(based on conditions).'''

# For Loop :
#For Loop in python is used to ierate over  the sequence(list, set, string,,dict) or other iterable objaects.

# to iterate over a character is called traversal.

# example :
n = 4
for i in range(0,n):
    print((i))

l = [10,20,30,40,50,60,70,80]
sum = 0
for i in l:
    sum+=i
    print(i)
print(sum)


l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
 print(l)
    #List
l = ["Hello","Good","Morning"]
for i in l :
    print(i)
    #Tuple
t = ("Hello","Good","Morning")
for i in t:
    print(i)

   #String
s = "Hello"
for i in s :
    print(i)

    # Dict
d = ({'x' : 10, 'y': 20})
for i in d:
    print("%s %d " %(i,d[i]))

    #Set

Set1 = {10,20,30}
for i in Set1:
    print(i)

# iteration by index of sequences :
''' In python we can also use index of elements in the sequence to iterate. the key idea is to first calculate 
 the length of the list and then iterate over the sequence within the range of this length'''

l = ["Hello", "Good","Morning"]
for index in range(len(l)):
    print(l[index])
