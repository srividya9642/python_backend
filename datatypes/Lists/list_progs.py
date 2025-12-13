# 1. Find the sum and average of elements:

numbers = [10,20,30,40,50]
print('sum:', sum(numbers))
print('Average:',sum(numbers) / len(numbers))


# Find the largest and smallest element(with built-in method)
nums = [12,5,8,19,3]
print('largest:',max(nums))
print('smallest:', min(numbers))

# find largest
nums = [12,5,8,19,3]
largest_val = smallest_val=  nums[0]
for n in nums:
    if n > largest_val:
        largest_val = n
    if n<smallest_val:
        smallest_val = n
print('Largest:',largest_val,'smallest:',smallest_val)



# Reverse a list with method
nums = [1,2,3,4]
nums.reverse()
print(nums)

# without built-in method
nums = [1,2,3,4]
rev = []
for i in range(len(nums) -1, -1, -1):
    rev.append(nums[i])
print(rev)

# 3. Remove duplicates with built-in method
nums = [1,2,2,3,3,4]
unique = list(set(nums))
print(unique)

# without built-in method
nums = [1,2,2,3,3,4]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)




