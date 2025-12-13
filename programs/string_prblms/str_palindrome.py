def is_palindrome(string):
    string = string.lower()  # make it case-insensitive
    reversed_str = ""
    
    # reverse the string manually
    for ch in string:
        reversed_str = ch + reversed_str

    # check if original equals reversed
    if string == reversed_str:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# take input from user
text = input("Enter a string: ")
is_palindrome(text)


def is_palindrome(str):
    str = str.lower()
    reversed_str = ""
    for ch in str:
        reversed_str = ch + reversed_str
        if str == reversed_str:
            print("the string is palindrome")
        else :
            print("String is not palindrome")
text = input("Enter a string")
is_palindrome(text)


def is_palindrome(str):
    str = str.lower()
    reversed_str = ""
    i = 0
    while i < len(str):
        reversed_str = str[i]
        if str == reversed_str:
            print("string is palindrome")
        else :
            print("String is not palindrome")
text = input('Enter a string')
is_palindrome(text)



def is_palindrome(str):
    str = str.lower()
    left = 0
    right = len(str)-1
    while left < right:
        if str[i] != str[right]:
            return False
        left +=1
        right -=1
    return True

text = input("Enter a string")
if is_palindrome(text):
    print(f"'{text}' is a palindrome")
else :
    print(f"'{text}' is not a palindrome")
    