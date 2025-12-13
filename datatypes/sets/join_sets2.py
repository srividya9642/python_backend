# The intersection() method : This method keeps ONLY the duplicates.
''' This method will return a new set, that only contains the items that are present in both sets.'''

set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}

set3 = set1.intersection(set2)
print(set3)



#Example 2
#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)


# We can also use '&' operator instead of intersection(), method.abs

set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}

set3 = set1 & set2
print(set3)



# Intersection_update(): method will also keep ONLY duplicates, but it will change the original set instead of returning a new set.

set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}

set1.intersection_update(set2)
print(set1)


# Difference :
''' the difference() method will retrun a new set that will contain only the items
from the first set that are not present in the oether set.'''

set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}

set3 = set1.difference(set2)
print(set3)


# by using '-' operator :
set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}

set3 = set1 - set2
print(set3)


# Difference_update ; This method also keep the items from the first set that are not in the second set,but it will change the
# original set instead of returning a new set.


set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}
set1.difference_update(set2)
print(set1)




# Symmetric Differences :
# The method will keep only the elements that are NOT present in both sets.


set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}

set3 = set1.symmetric_difference(set2)
print(set3)

# by using the '^' operator 
set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}
set3 = set1 ^ set2
print(set3)


# Syemmetric_difference_update() :
''' this method also keep the elements which are not present in both sets(duplicates), 
but it will change the original set,instead of returning a new set.'''

set1 = {'apple','banana','cherry'}
set2 = {'google','microsoft','apple'}
set1.symmetric_difference_update(set2)
print(set1)