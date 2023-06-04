list = [7,2,12,8,3]
print(list)
arrLen = len(list)
for i in range(arrLen):
    for index in range(arrLen - 1):
        if (list[index] > list[index+1]):
            temp = list[index]
            list[index] = list[index + 1]
            list[index + 1] = temp
    arrLen = arrLen - 1
print(list)
