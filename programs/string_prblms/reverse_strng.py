# write a program to reverse a string

string1 = "python"
reversed_string = " "
i = 0
for ch in string1:
    reversed_string = ch + reversed_string
    i+=1
print(reversed_string)


# while loop
text = 'python'
reversed_string = ''
i = len(text)-1
while i >=0:
    reversed_string += text[i]
    print(reversed_string)
    i-=1
    

print(reversed_string)

# using function

def reversed_string(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev += str[i]
    return rev

print("reversed string:",reversed_string(input("Enter string")))


def reversed_string(str):
    rev = ''
    i = len(str)-1
    while i >= 0:
        
        rev += str[i]
        i -=1
        return rev
print("reversed string:",reversed_string(input("Enter the text")))


