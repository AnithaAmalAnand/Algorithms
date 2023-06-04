list = [96,74,55,30,65,41,89]
print (list)
for index in range(1,len(list)):
    temp = list[index]   # get the value at that index
    # compare to each item to the left
    i = index - 1
    while i >=0:
        if temp < list[i]:
            list[i+1]=list[i]
            list[i]=temp
            i = i - 1
        else:
            break;
print(list)
    
