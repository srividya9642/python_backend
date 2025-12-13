my_list = [1,2,3,4,5]
k = 2
for i in range(k):
    last = my_list.pop()
    my_list.insert(0,last)
    
print("Rotated List:",my_list)