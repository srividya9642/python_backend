my_tuple = (1,2,3,2,4,2,5)
element = 0
count = 0
i = 0
while i < len(my_tuple):
    if my_tuple[i] == element:
        my_tuple[i] +=1
        count +=1
        i +=1
        
print("The occurrence is:",count)