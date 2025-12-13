# Frozenset:
''' frozenset is an immutable version of set.
like sets,it contains unique, unordered,unchangable elements.
unlike sets, elements cannot be added or removed from a frozenset. '''


# Creating a frozenset:  we can use the frozenset() constructor to create a frozenset from any iterable.

x = frozenset({'apple','banana','cherry'})
print(x)
print(type(x))

# Frozenset methods() :

# 1. copy() : returns a shallow copy.
fs = frozenset({1,2,3})
cp = fs.copy()
print(fs)
print(cp)


# 2. difference() : '-' returns a new frozenset with the difference.
a = frozenset({1,2,3,4})
b = frozenset({3,4,5})
print(a.difference(b))
print(a - b)

# 3. intersection() : '&' returns a new frozenset with the intersection.
a = frozenset({1,2,3,4})
b = frozenset({3,4,5})
print(a.intersection(b))
print(a & b)


# 4. isdisjoint() : returns whether two frozensets have an intersection.
a = frozenset({1,2})
b = frozenset({3,4})
c = frozenset({2,3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))


# 5. issubset() : <=/< returns True if this frozenset is a (proper) subset of another.
a = frozenset({1,2})
b = frozenset({1,2,3})
print(a.issubset(b))
print(a<=b)
print(a<b)

# 6. issuperset() : >=/> returns True if this frozenset is a (proper) seperset of another.
a = frozenset({1,2,3})
b = frozenset({1,2})
print(a.issuperset(b))
print(a>=b)
print(a>b)

# 7. symmetric-difference() : '^' Returns a new frozenset with the symmetric differences.
a = frozenset({1,2,3})
b = frozenset({3,4,5})
print(a.symmetric_difference(b))
print(a ^ b)

# 8. union(): '|' Returns a new frozenset containing the union
a = frozenset({1,2})
b = frozenset((2,3))
print(a.union(b))
print(a | b)