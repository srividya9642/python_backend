# what is find
''' fine is a method it is used to find out the occured specified value in a string'''

text = "Pyhton programming"
print(text.startswith("programming"))



text = "Hello, Good Morning"
print(text.find('o'))

text = "I love mangoes, mangoes are sweetest"
print(text.find('e', 24,27))


text = "Python@123"
print(text.isalnum())

text = "Python1"
print(text.isalpha())

numbers = "123456"
print(numbers.isdigit())

num1 = "123.55"
print(num1.isdigit())

# islower():
text = "python is fun! "
print((text.islower()))


# isupper():
Text = "PYTHON is fun!"
print(text.isupper())


# isnumeric()
nums = "123456"
print(nums.isnumeric())

# isspace()
text = ""
print(text.isspace())


# istitle () ;
'''The method  title will return true if the the  the string is properly title cased (starting character in every word should be capital(, otherwise false'''
Text = "Python, Is Easy To Learn"
print(Text.istitle())

Text = "Nikhil is learning"
print(Text.count('i'))

# count() :
'''The method count will count the number of times the specified value occured in a strng'''
Text = " Python is easy to learn"
print(Text.count('o'))

# find()
''' The method find() is used to find the index of the first occurance in a string with another string'''
Text = " Python is easy to learn"
print((Text. find('n')))


#capitalize( )

'''The metod capitalize will convert the first letter of string to upper case and the rest  of the word to thr lowrrcase'''
Text = "hello good morning!"
print((Text.capitalize()))

# swapcase()
''' The method swapcase will return the the string where all letters in a string to upper to lower and lower to upper'''

Text = "Hello Good Morning!"
print(Text.swapcase())


# Reverse a string
''' to rever a string we do not have any bilt=in function, but we can reverse a string by using the slicing backward(backward slicing -1)'''
Text = "Hello world!"
reversed_text = Text[::-1]
print(reversed_text)


# To reverse a string we can also use the reverse function

Text = "Python"
reversed_text = ' '. join(reversed(Text))
print(reversed_text)


# lower()
''' The method lower will convert the  string to uppercase'''
Text = "HELLO WORLD!"
print(Text.lower())

#upper()
'''' The method upper wil convert  the sting to lowercase. '''

text = "Python is fun!"
print(text.upper())



import sys

'''x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print(z)'''



'''import sys
args = sys.argv'''

Name = "Hello World!"
print(Name)




Text = "Python"
print(Text[::-1])

string = "Good Morning"
print(string.replace("o", "r"))


# reverse a string
s = "Hello"
reverse_string = ""
i = len(s) - 1
while i >=0 :
    reverse_string = reverse_string + s[i]
    i -= 1

print( "Reversered string:", reverse_string)



S =  "Hello"
reverse_string = ""
i = len(s)-1
while i >=0 :
    reverse_string = reverse_string + s[i]
    i -= 1

print("Reversed string :", reverse_string)
