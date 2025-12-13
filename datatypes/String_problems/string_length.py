# To print the length of the string
#  by sing the len() function
a = "Hello"
print(len(a))



#Using for loop and 'in' operator

a = "Hello"
count = 0

# Loop through each character in the string 'a'
for char in a:
   # Increment 'count' by 1 for each character
    count += 1
print(count)



# using str.count()
a = "Hello"

# It counts the number of occurrences of the specifies substrings
length = a.count('') - 1
print(length)


# by using numerate () function

''' The enumerate() function will loop over an iterable and keep track of the index 
and the value of the elements within that iterable'''
a = "hello"
s = 0
for i, a in enumerate(a):

    s +=1
    print(s)
