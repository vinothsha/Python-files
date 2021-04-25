'''a=[1000,999,345,900,400,397]
size=len(a)
for k in range(10):
    for i in range(size-1):
        for j in range(size-1):
            if a[j]>a[j+1]:
                #a[j],a[j+1]=a[j+1],a[j]
                tem=a[j]
                a[j]=a[j+1]
                a[j+1]=tem
print(a)'''
a=[1000,999,345,900,400,397]
size=len(a)
for i in range(size):
    for j in range(size-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
