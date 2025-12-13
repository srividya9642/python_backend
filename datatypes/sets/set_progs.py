# 1. Find unionand intersection by using the built-in methods.

A = {1, 2, 3}
B = {3, 4, 5}
print('union:',A.union(B))
print('intersection:',A.intersection(B))

# without using the built-in method :
A = {1, 2, 3}
B = {3, 4, 5}

union = set(A)
for i in A:
    if i in B :
        union.add(i)
        
intersection = set()
for i in A:
    if i in B :
        intersection.add(i)
        
print('union:',union)
print('intersection:',intersection)

# 2.check subset by using built-in method :
A = {1,2}
B = {1,2,3}
print(A.issubset(B))

# Without using the built-in method:

A = {1,2}
B = {1,2,3}
subset = True
for i in A :
    if i not in B:
        subset = False
        
print(subset)