# write a program to convert a string to uppercase and lowercase

def upper_string(str):
   result = ""
   for ch in str:
       if 'A' <= ch <= 'Z':
           result += chr(ord(ch) - 32)
       else:
           result += ch
   return result


def lower_string(str):
    result = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result
            
            
text = input("Enter a string")
upper_text = list(upper_string(text))
lower_text = lower_string(text)

print("Original string:",text)
print("To uppercase:",upper_string)
print('To lowercase:',lower_string)            


            
            
            
        