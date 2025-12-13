# We can access the tuple items by referring to the index numbers, inside the square brackets :
# Print the second itemmin the tuple ;

thistuple = ("apple","banana","cherry")
print(thistuple[2])

# Negative indexing :

thistuple = ("apple","banana","cherry")
print(thistuple[-1])

# Range of index :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1:4])


# ex : by leaving out the start value,  the range will start at the first item :

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# ex : by leaving out the end value, the range will go on to the end of the tuple :

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# Range if negative indexing :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[-4 :-1])


# check if item exists :    check if 'apple present in the tuple.
thistuple = ('apple','banana','cherry')
if 'apple' in thistuple:
    print("Yes")