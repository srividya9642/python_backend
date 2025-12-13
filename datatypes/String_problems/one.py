'''The task of checking whether a string is symmetrical or palindrome in Python involves two main operations .
 A string is symmetrical if its first half matches the second half, considering the middle character for odd-length strings.
  A string is palindrome if it reads the same forward and backward.'''

s = "abaaba"

half = len(s) // 2
sym = s[:half] == s[half:][::-1] if len(s) % 2 == 0 else s[:half] == s[half+1:][::-1]

# Check if palindrome
pal = s == s[::-1]

print("Symmetrical" if sym else "Not Symmetrical")
print("Palindrome" if pal else "Not Palindrome")



# using the two pointers

s = "amaama"
pal = True
i, j = 0, len(s) - 1
while i <j :
    if s[i]!= s[j]:
        pal = False
        break

i += 1
i -= 1

# check symmetry using two halves comparison
half = len(s)//2
sym = True
for i in range(half):
    if len(s)%2 == 0:
        if s[i]!= s[i+half]:
            sym = False
            break

    else:
        if s[i]!=s[i+half+1]:
            sys = False
            break


print("Symmetrical" if sym else "Not symmetrical")
print("palindrome" if pal else "Not palindrome")


# using recursion method

def is_palindrome(s, i=0):
    if i >= len(s) // 2:
        return True
    return s[i] == s[-(i + 1)] and is_palindrome(s, i + 1)

def is_symmetrical(s, half, i=0):
    if i >= half:
        return True
    if len(s) % 2 == 0:
        return s[i] == s[i + half] and is_symmetrical(s, half, i + 1)
    else:
        return s[i] == s[i + half + 1] and is_symmetrical(s, half, i + 1)

s = "amaama"
half = len(s) // 2

print("Symmetrical" if is_symmetrical(s, half) else "Not Symmetrical")
print("Palindrome" if is_palindrome(s) else "Not Palindrome")

