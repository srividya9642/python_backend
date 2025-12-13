# print the len of the given string

def string_length(str):
    count = 0
    for ch in str:
        count += 1
    return count
print(string_length(input('Enter the string')))