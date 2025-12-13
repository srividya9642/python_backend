# write a progrm to remove all vowels from the string without uing the built-in methods

def remove_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for ch in input_string:
        is_vowel = False
        for char in vowels:
            if ch == char:
                is_vowel = True
                break
        if not is_vowel:
            result = result + ch
    return result

# Example usage
user_input = input("Enter a string: ")
output = remove_vowels(user_input)
print("String without vowels:", output)




def remove_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    for ch in input_string:
        if ch not in vowels:
            result = result + ch
    return result
user_input = input("Enter a string:")
output = remove_vowels(user_input)
print("string without vowels:",output)

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in user_input:
        if ch not in vowels:
            result = result + ch
    return result

user_input = input("Enter a string")
output = remove_vowels(user_input)
print("String without vowels:",output)




def remove_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    i = 0
    
    while i < len(input_string):
        ch = input_string[i]
        if ch not in vowels:
            result = result + ch
        i = i + 1   # move to next character
    
    return result

# Example usage
user_input = input("Enter a string: ")
output = remove_vowels(user_input)
print("String without vowels:", output)