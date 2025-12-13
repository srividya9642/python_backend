# Python has a set of built-in methods that we can use on strings.

# All string methods return new values.They do not change the original string.

# capitalize () : This method will return a string where the first character is uppercase.
text = "hello, welcome to my world!"
x = text.capitalize()
print(x)

# casefold() : this method will return a string where all the characters are lower case.
text = "Hello, Welcome To My World!"
x = text.casefold()
print(x)

# center : Thi method will center align the string, using a specified character(space is default) as the fill character.
text = "Hello"
x = text.center(20)
print(x)

# encode : The encode method encodes the string, using the specified encoding. if no coding is specified. UTF -8 will be used.
text = 'Hello world'
x = text.encode()
print(x)

# count() : The count method returns the number of times a specified value appears in the string.
text = "I apples, apple are my favorrite fruit"
x = text.count('apple')
print(x)

# endswith(): return True if the string endswith the specified value,oetherwise False.
text = "Hello, welcome to my world"
x = text.endswith('world')
print(x)

# startswith() : return True if the string startswith the specified value,oetherwise Flase.
text = "Hello, welcome to my world"
x = text.startswith('Hello')
print(x)

# find() : 
''' The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index()
method raises an exception if the value is not found.'''

text = "Hello, welcome to my world!"
x = text.find("e")
print(x)

# Ex :2 
text = "Hello, welcome to my world"
x = text.find('e',5,10)
print(x)

# If the value is not found the find() returns -1, but the index() method will raise an error:
text = "Hello,welcome to my world"

print(text.find('q'))
print(text.index('q'))


# format():

''' the format() method formats the specified value and insert tem inside the string's placeholder.

The placeholder is defined using curly brackets :{}. Read more about the placeholders in the placeholder section.


The format() method returns the formatting string.'''
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# The placeholders : the placeholders can be identified using name indexes {price}, numbered indexes {0},
# or even empty placeholders {}.

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)


