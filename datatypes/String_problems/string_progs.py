# 1. reverse a string by using method,
s = 'python'
print(s[::-1])

# without using the method.
s = 'python'
reversed_string = ""
for item in s:
    reversed = item + reversed_string
print(reversed_string)

# by using while loop
string = 'python'
reversed_string = ""
i = len(string) -1
while i >= 0:
    reversed_string += string[i]
    i-=1
print(reversed_string)


# Count Vowels with built-in method:
s = 'HelloWorld'
vowels = 'aeiouAEIOU'
print(sum(ch in vowels for ch in s))

# without built-in method :
s = 'HelloWorld'
vowels = 'aeiouAEIOU'
count = 0
for ch in s :
    if ch in vowels:
        count += 1
print('vowels:', count)

# 3 . check palindome  with built-in method:
s = "madam"
if s == s[::-1]:
    print('Palindrome')

# withot built-in method:
s = 'madam'
rev = ''
for ch in s:
    rev = ch + rev
if s == rev:
    print('palindrome')