'''class sha:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def ad(self,other):
        return complex(self.a+other.a,self.b+other.b)
s=sha(1,2)
s1=sha(3,4)
print(sha.ad(s,s1))'''

class person:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'str call '+self.a+self.b
    def __repr__(self):
        return f'repr call {self.a}'
    def __add__(self,other):
        return self.a+self.b+other.a+other.b
a=person('vin','sha')
print(str(a))
print(repr(a))
#int pass to add function
b=person(1,2)
c=person(3,4)
print(b+c)
#str pass to add function
x=person('sha','vin')
y=person('billa','kannan')
print(x+y)












