# Write a program to find the frequecy of each character in a string

def find_character_frequencies(str):
    freq= {}
    for ch in str:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    return freq

text = input("Enter a string")
result = find_character_frequencies(text)

print("The character frequency is:",result)

