from functools import partial
def email(id,domain,extension):
    return id+domain+extension
par=partial(email,'kvinothsha')
par1=par('@gmail','.com')
print(par1)

def add(a,b,c):
    return a+b,a*b+c
a=partial(add,5)
a1=a(2,3)
print(a1)

