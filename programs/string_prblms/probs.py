# 1. reverse a given string 

sentence = input("Enter a string:") # Input sentence

words = sentence.split() # split the sentence into words

reversed_words = words[::-1] # Reverse the list of words

reversed_sentence = " ".join(reversed_words) # Join them back into a sentence

# Displaying result
print("Original sentence:",sentence)
print("Reversed sentence:",reversed_sentence)


#  reverse a given string without using built-in methods.

string = input("Enter a string")
reversed_string = string[::-1]
print(reversed_string)


string = input("Enter a string")
reversed_string = "".join(reversed(string))
print("Reversed string is:",reversed_string)

#2. Write a program to count the number of vowels in a string
string = input("Enter a string")
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count +=1
  

print("the string contains:",count)

    
# 3 .check whether a given string is palindrome or not
string = input("Enter a string : ")
# convert the string to lowercase and  remove spaces
string = string.replace(" ","").lower()

#  Reverse the string using slicing
reversed_string = string[::-1]
# check if the given string is equal to the reversed string
if string == reversed_string:
    print("The given string is palindrome")
else:
    print("Not a palindrome")


# 4.. write a program to count number of uppercase and lowercase letters in a string
string = input("Enter a string")

upper_count = 0   # Taking the count as lower and upper '0
lower_count = 0
for ch in string:   # l0op thorugh the each character
    if ch.isupper(): # check if the char is upper and increase the count by '1'
      upper_count +=1
    elif ch.islower():
        lower_count +=1
        
print("Uppercase letters:",upper_count)
print("Lowercase letters:",lower_count)



# 5 write a program to find the length of the string

string = input("enter a string :")

string_length = len(string)
print(string_length)

# using for loop
string = input("Enter a string:")
count = 0
for ch in string:
    count +=1
print("length of string:",count)


# using while loop
string = input("Enter a string:")  
count= 0
while True:
    try:
        string[count]
        count +=1
    except IndexError:
        break
print("Length of string:",count)


# 6.rite a program to replace all spaces in a string with '-'abs

string =input("Enter a string:")
replace_string = string.replace(' ',"-")
print("The replaced string is:",replace_string)

# using split and jon method
string = input('Enter a string:')
replace_string = tring.split()
new_string = "-".join(replace_string)

print("String after replacing:",new_string)
# using list comprehension

string = input("Enter a string")
new_string = ''.join(['-' if char == '' else char for char in string])

print(new_string)                                                  

# 7. find how many times a particular character appears in a string.

# Define the input string
text = "Apples are amazing!"

# Define the character to count
char_to_count = 'a'

# Use the count() method
count = text.count(char_to_count)

# Print the result
print(f"The character '{char_to_count}' appears {count} times.")

# 8. convert a string to uppercase and lowercase

text = input("Enter a string")

uppercase_text = text.upper()
lowercase_text = text.lower()
print("Uppercase:",uppercase_text)
print("Lowercase:",lowercase_text)



# 9.write a program to remove all vowels from a string

string = input("Enter a string")

vowels = "aeiouAEIOU"
for vowel in vowels:
    string = string.replace(vowel,"")
    
print("Without vowels:",string)

# using list comprehension

text = input("Enter a string")
vowels = 'aeiouAEIOU'

result = ''.join([char for char in text if char not in vowels])

print("Without vowels:",result)



#10. concatenate two strings without using '+' operator 

def concatenate_strings(str1,str2):
    result = ""
    for ch in str1:
        result = result + ch
    for ch in str2:
        result = result + ch
        
    return result

s1 = input('Enter string 1')
s2 = input("Enter string 2")
output = concatenate_strings(s1,s2)

print("concatenation of two strings :", output)

# by using join method
str1 = " Hello "
str2 = " world "

result = "".join([str1,str2])
print("concatenated string:",result)

# using format()

str1 = " hello "
str2 = " world "

result = "{}{}".format(str1,str2)
print("concatenated string:",result)

# write a program to count the number of words in a string

string = input("Enter a string")

words_coount = len(string.split())
print("Number of words:",words_coount)


# Using dict to store as key value pairs
string = input("Enter a string")
freq = {}
for ch in string:
    if ch in freq:
        freq[ch] +=1
    else :
        freq[ch] = 1
return freq
print("The count of the string is:",string)









