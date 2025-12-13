# 1. Find max in min with the built-in method:

t = (5,10,3,9)
print('Max:', max(t))
print('Min:', min(t))

# Without built-in method

t = (5,10,3,9)
max_val = min_val = t[0]
for n in t:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n
print('Max:', max_val, 'Min:', min_val)


# 2 , count occurances :
t = (1,2,2,3,3,3)
print('count of 3:',t.count(3))

# without built in method:
t = (1,2,2,3,3,3)
count = 0
for n in t :
     if n ==3:
         count += 1
print('count of 3:',count)