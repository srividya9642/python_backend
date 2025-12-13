# Write a program to count the upper and lower case letter in a string

def count_case(str):
    upper = 0
    lower = 0
    
    for ch in str:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
            
            
    print("Number of uppercase letters:",upper)
    print("Number of lowercase letters:",lower)
    
text = input("Enter a string")
count_case(text)

def count_case(str):
    upper = 0
    lower = 0
    
    for ch in str:
         if ch.isupper():
             upper +=1
         elif ch.islower():
             lower +=1
             
    print("Number of uppercase letters;",upper)
    print("Number of lowercase letters:",lower)

text = input("enter a string")
count_case(text)


def count_cases(str):
    upper = 0
    lower = 0
    for ch in str:
        if 'A' <= ch <= 'Z':
            upper +=1
        elif 'a' <= ch <= 'z' :
            lower +=1
    print('Number of uppercase letter:',upper)
    print('Number of lowercase letters:',lower)
    
text = input("Enter a string")
count_cases(text)



def upper_lower_count(str):
    upper = 0
    lower = 0
    for ch in str:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print('Number of uppercase letters:',upper)
    print('Number of lowercase letter:',lower)
    
    text = input("Enter a string")
    upper_lower_count(text)