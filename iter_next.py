'''a=[1,2,3]
s=a.__iter__()
print(s.__next__())
print(s.__next__())
print(s.__next__())
#or
print('another method')
b=[4,5,6]
x=iter(b)
x=iter(b)
x=iter(b)
print(next(x))
print(next(x))
print(next(x))'''

#def fact(n):
    #return n*fact(n-1) if n else 1
    #return 1 if n==1 or n==0 else n*fact(n-1)
    #return 1 if n==0 else n*fact(n-1)
#print(fact(5))

from datetime import datetime
def fact(n):
    if n:
        return n*fact(n-1)
    else:
        return 1
start=datetime.now()
print(start)
print(fact(5))
print(fact(8))
print(fact(10))
end=datetime.now()
print(end)
print(end-start)



