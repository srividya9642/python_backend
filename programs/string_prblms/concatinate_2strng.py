# write a program to concatinate two strings without using '+' operator 




def concatenate_strings(str1,str2):
    result = ""
    for ch in str1:
        result = result + ch
    for ch in str2:
        result = result + ch
        
    return result

s1 = input('Enter string 1')
s2 = input("Enter string 2")
output = concatenate_strings(s1,s2)

print("concatenation of two strings :", output)


def concatenate_strings(str1,str2):
    result = ""
    i = 0
    result_list = []
    while i <len(str1):
     result_list.append(str1[i])
     i +=1
     j = 0
    while j <len(str2):
        result_list.append(str2[j])
    j +=1
    k = 0
    while k <len(str2):
        result = result_list[k]
        k +=1
        
    return result

s1 = input("Enter string 1")
s2 = input("Enter string 2")

output = concatenate_strings(s1,s2)
print("Concatenating two strings :",output)




def concatenate_strings(str1,str2):
    result = ""
    for ch in str1:
        result += ch
    for ch in str1:
        result += ch
    return result

s1 = input("Enter string 1")
s2 = input("Enter string 2")

output = concatenate_strings(s1,s2)
print('concatenating two strings:', output)

def concatenate_strings(str1,str2):
    result = ""
    result_list = []
    while i <len(str1):
        result_list.append(str1[i])
    j = 0
    while j <len(str2):
        result_list.append(str2[j])
    k = 0
    while k < len(str2):
        result = result_list[k]
        k +=1
    return result


s1 = input("Enter string 1")
s2 = input("Enter string 2")
output = concatenate_strings(s1,s2)

print("Concatenating strings:", output)

