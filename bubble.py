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

'''a=[1000,999,345,900,400,397]
size=len(a)
for i in range(size):
    for j in range(size-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)'''

def bubble_sort(elements, key=None):
    size = len(elements)
    for i in range(size-1):
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
    print(elements)
if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, key='transaction_amount')
