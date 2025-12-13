# Write a program to check how many time a character appears in a string

def count_chars(str,ch):
    count = 0
    for c in str:
        if c == ch:
            count += 1
    return count

text = input(" Enter a string")
char = 'p'
result = count_chars(text,char)
print(f"The character'{char}' appears {result} times in '{text}'.")




def count_chars(str,ch):
    count = 0
    i = 0
    while i <len(str):
        if str[i] == ch:
            count +=1
        i +=1
    return count

text = input(" Enter a string")
char = 'g'
result = count_chars(text,char)
print(f"The character'{char}' appears {result} times in '{text}'.")




