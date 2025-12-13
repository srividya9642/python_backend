# Write a program to Check whether a string contains only digits (without using .isdigit()).

def is_digits(str):
    digits = '0123456789'
    for ch in str:
        if ch not in digits:
            return False
        
    return True

text = input("Enter a string")

if is_digits(text):
    print("The string contains only digits.")
else:
    print("The string contains other characters also.")




