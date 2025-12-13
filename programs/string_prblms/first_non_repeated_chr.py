# write a program to find first non repeated characters in string

def first_non_repeated_char(string):
    for ch in string:
        count = 0
        for other in string:
            if ch == other:
                count += 1
        if count == 1:
            return ch   # found the first non-repeated character
    return None   # if no unique character found



text = input("Enter a string: ")
result = first_non_repeated_char(text)

if result:
    print("First non-repeated character is:", result)
else:
    print("No non-repeated character found.")

            
            
    
# Using dictionary

def first_non_repeated_char(str):
    freq = {}
    for ch in str:
        if ch in freq:
            freq[ch] +=1
        else:
            freq[ch] = 1
            
    for ch in str:
        if freq[ch] == 1:
         return freq
    
    return None

text = input("Enter a string")
result = first_non_repeated_char(text)

if result:
    print("First non repeated character:",result)
else:
    print("No first non repeated character")
    
    
    
    
    
string = input("Enter a string: ")

i = 0
found = False
while i < len(string):
    ch = string[i]
    j = 0
    count = 0
    
    while j < len(string):
        if string[j] == ch:
            count += 1
            j += 1
            
            
    if count == 1:
       print("First non-repeated character is:",ch)
       found = True
       break

    i += 1

if not found:
    print("No non-repeated character found.")    
    
    
    
    
    


