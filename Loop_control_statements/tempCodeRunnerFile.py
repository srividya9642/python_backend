i = 0
while i < 10 :
    if i == 5 :
        i += 1 # ensure that loop variable is incremented to avoid infinite loop
        continue
    print(i)
    i +=1