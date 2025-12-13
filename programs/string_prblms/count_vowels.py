def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in str:
        if ch in vowels:
            count += 1
    return count
print("number of vowels:",count_vowels(input("Enter a string")))


def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    i = 0
    while i <len(str):
        if ch in vowels:
            count +=1
            i +=1
        return count
print("vowels count:",count_vowels(input("Enter a string")))