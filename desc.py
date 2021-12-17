num = [5,3,9,7,2]
s=[]
for i in range(len(num)):
    for j in range(i,len(num)):
        if num[i] > num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
       # print(num[i],end='\t')
    s.append(num[i])
print(s)