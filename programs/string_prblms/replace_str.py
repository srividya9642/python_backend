def replace_spaces(str):
    new_string = ""
    for ch in str:
        if ch == " ":
            new_string += "-"
        else :
            new_string += ch
            
    return new_string
text = input('Enter a string')
result = replace_spaces(text)
print('result:',result)
            
            
            
            
            
            
            
def replace_spaces(str):
    new_str = ""
    for ch in str:
        if ch == " ":
           new_str += "-"
        else:
            new_str += ch
    return new_str

text = input('Enter a string')
result = replace_spaces(text)
print('Result:',result)



def replace_spaces(str):
    new_string = ""
    i = 0
    while i < len(str)-1:
        if str[i] == "" :
            new_string += " - "
        else:
            new_string += str[i]
    return new_string
text = input("Enter a string")
result = replace_spaces(text)
print("result:",result)

def replace_spaces(str):
    new_string = ""
    for ch in str:
        if ch == "":
            new_string += "-"
        else :
            new_string += ch
    return new_string

text = input("Enter a string")
result = replace_spaces(text)
print("Result:",result)
            
            
            
def replace_spaces(str):
    new_string = ""
    i = 0
    while i <len(str)-1:
        if str[i] == "":
            new_string += "-"
        else :
            new_string += str[i]
    return new_string
text =input("Enter a string")
result = replace_spaces(text)
print("Result:",result)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            