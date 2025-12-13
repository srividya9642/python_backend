# reverse  words in a Given string in python
# Using spilt()  and join()

a = "Good Morning"

# Split the string into words, reverse the list of words, amd  join them back

reversed_words = ''.join(a.split())[::-1]
v
print(reversed_words)


# Using for loop
a = "Good Morning"

words = a.split()
reversed_words = ""

for word in reversed(words):
    reversed_words += word + " "

reversed_words = reversed_words.strip()

print(reversed_words)






string = 'python'
reversed_string = ""
i = len(string) -1
while i >= 0:
    reversed_string += string[i]
    i-=1
print(reversed_string)
    
text = 'python'
reversed_string = ""
for char in text:
    reversed_string = char + reversed_string
print(reversed_string)



text = 'apple'
old_char = 'p'
new_char = 'b'
result = ""
for ch in text:
    if ch == old_char:
        result += new_char
    else :
        result += ch
print(result)


text = "python"
old_char = 'p'
new_char = 'c'
i = 0
result = ""
while i < len(text):
    if text[i] == old_char:
        result += new_char
    else:
        result += text[i]
print(result)
        