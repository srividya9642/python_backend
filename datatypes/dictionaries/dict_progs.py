# 1. count frequency of characters with the built-in method:
s = 'banana'
freq = {}
for ch in s :
        freq[ch] = freq.get(ch,0) + 1
print(freq)

from collections import Counter
s  = 'banana'
print(dict(Counter(s)))
    

# without using built-in method.
s = 'banana'
freq = {}
for ch in s :
    if ch in freq:
        freq[ch] += 1
    else :
        freq[ch] = 1
        
print(freq)

# 2. merge two dictionaries.

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
d1.update(d2)
print(d1)

# Find key with maximum value :
marks = {'A':85, 'B':90,'c':75}
max_key = max(marks, key=marks.get)
print('Topper:', max_key)

# Conver two lists into dictionary
keys = ['name','age','city']
values = ['vidya','22','bangalore']
d = dict(zip(keys,values))
print(d)


# sort dictionary by value:

data = {'a':5,'b':2,'c':8}
sorted_data = dict(sorted(data.items(), key = lambda x: x[1]))
print(sorted_data)


# check if key exists

student = {'name': 'vidya','age':21}
if 'age' in student:
    print('Key exists')
else:
    print('Key not found')