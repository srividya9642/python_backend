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



s =  "Hello"
reverse_string = ""
i = len(s)-1
while i >=0 :
    reverse_string = reverse_string + s[i]
    i -= 1

print("Reversed string :", reverse_string)



text = "Python"
reverse_string = ""
for char in text:
    reverse_string = char + reverse_string
    print(reverse_string)
    
    
    
text = "python"
reverse_string = ""
i = len(text)-1
while i >=0:
    reverse_string = reverse_string + text[i]
    i -=1
print(reverse_string)


text = "python"
old_char = 'p'
new_char = 's'
result = ""
for ch in text :
    if ch == old_char:
        result += new_char
    else :
        result += ch
print(result)



text = 'python'
old_char = 'p'
new_char = 's'
i = 0
result = ""
while i < len(text):
    if text[i] == old_char:
        result += new_char
        
    else :
        result += text[i]
        i+=1
print(result)