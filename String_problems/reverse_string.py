# reverse  words in a Given string in python
# Using spilt()  and join()

a = "Good Morning"

# Split the string into words, reverse the list of words, amd  join them back

reversed_words = ''.join(a.split())[::-1]

print(reversed_words)


# Using for loop
a = "Good Morning"

words = a.split()
reversed_words = ""

for word in reversed(words):
    reversed_words += word + " "

reversed_words = reversed_words.strip()



print(reversed_words)
