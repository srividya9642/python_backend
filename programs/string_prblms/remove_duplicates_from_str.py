# Write a program to remove duplicate characters from a string
def remove_duplicates(text):
    result = ''
    for ch in text:
        if ch not in result:
            result += ch
            
    return result
text = input("Enter a string: ")

print("The string after removing the duplicate values:",remove_duplicates(text))



def remove_duplicates(string):
    result = 0
    i = 0
    while i <len(string):
        ch = string[i]
        found = False
        j = 0
        while j <len(result):
            if result[j] == ch:
               found = True
               break
            j += 1
            
        if not found:
            result += ch
        i += 1
        
        
string = input("Enter a string")
print("String after removing duplicates:",remove_duplicates(string))