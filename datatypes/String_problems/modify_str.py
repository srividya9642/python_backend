# Python has a set of built-in methods that we can use on strings.abs

# Upper case : Return the string to the upper case
string1 = 'hello world'
print(string1.upper())

# Lower case : Return the string to the lower case
string1 = 'HELLO WORLD!'
print(string1.lower())

# Remove whitespace: Whitespace is th space before and/or after the actual text,
# and very often we want to remove the space.abs

string1 = " Hello, World "
print(string1.strip())

# Replace strimg ; The replace() method replace a string with another string:
string1 = "Hello"
print(string1.replace('H','J'))

# Split string : The spilt() method returns a list where the text between the specified separator becomes the list items.

string1 = 'Hello, world!'
print(string1.split(','))

# String concatination : To concatinate, or combine, two strings we can use'+' operator:

string1 = "hello"
string2 = 'World'
string3 = string1+ " " +string2
print(string3)


# String Format: As we learned in the variables chapters, we cannot combine strings and numbers.
age = 36
text = "My name is John, I am " + age
print(text) # error

# We can use f-srings or the format() method to combine strings and numbers.
''' To specify a string as an f-string, simply put an f in pront of the string literal,and add curly 
braces{} as placeholders for variales and other operations.'''

age = 22
text = f"My name is Sriividya, I am {age}"
print(text)

# Placeholders and modifiers : A place holder can contain variables operations,functions,
# and modifiers to format the value.

price = 60
text = f"The price is, {price} dollars"
print(text)

# A place holder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type,like.2f which means
# fixed point number with 2 decimals :


price = 59
text = f"The price is, {price:.2f} dollars"
print(text)


# A placeholder can contain python code,like math operations:

# example : perform a math operation in the placeholder, and return the result:

text = f"the prrice is{20 * 59} dollars"
print(text)


# Python escape characters :
''' To insert characters that are illegal in a string, we can use an escape character.
An escape chaacter is a backslash \ followed by the character we want to insert. '''

# ex :
text = "We are the so-called \"vikings\" from the North. "
print(text)


# Escape characters :

# \' : Single quotes :
text = 'It\'s alright.'
print(text)

# \\ : Backslash : 
text = "This will insert one \\ (backslash)."
print(text)
# \n : newline : 
text = "Hello\nworld!"
print(text)

#v\r : Carriage Return :
txt = "Hello\rWorld!"
print(txt) 
# \t : Tab :
text = "Hello\tWorld"
print(text)

# \b : Backspace: This example erases one character(backspacse):
text = "Hello\bWorld!"
print(text)

# \f : form feed ;
# \ooo : Octal value : A backslash followed by three intergers will result in a octal value :
text = "\110\145\154\154\157"
print(text)

#\xhh : hex value : A backslash followed by an 'x' number represents a hex value:
text = "\x48\x65\x6c\x6c\x6f"
print(text)
