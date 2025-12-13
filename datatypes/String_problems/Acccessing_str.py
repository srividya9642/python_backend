# Accessing  characters in string
''' Strings are indexed sequences. Positive indes is starts from 0 and the negative
indes is starts from -1 which the backward of the string.'''

s = "Hello"
print(s[1])
print(s[3])

# Uisng negative indexing
s = "Goodmorning"
print(s[-6])
print(s[-4])

# Looping through a string
string1 = "Hello"
for x in string1:
    print(x)
    
# To get the length of the string, we can use the len() function.
string1 = 'Hello'
print(len(string1))

# To check if a certain phrase or character is prrsent in s string, we can use the keyword 'in':

string1 = "Hello world!"
print('world' in string1)
# using if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#Check if NOT :

string1 = "Hello Python"
print('expensive' not in string1)


string1 = "Hello Python"
if 'world' not in string1:
    print(" No,'expensive' not in python")
