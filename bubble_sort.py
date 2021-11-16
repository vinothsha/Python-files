a=[5,1,4,77,11,2]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)