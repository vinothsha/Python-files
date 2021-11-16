def add2(n):
    if n==0:
        return 0
    else:
        return 2 +add2(n-1)
print(add2(1))
print(add2(2))
print(add2(3))
print(add2(4))