n=input('Введите строку\n')
a=input('Введите цепочку символов для нахождения:\n')
n=n.replace(' ','')
def find (n,a):
    count = 0
    b=0
    while b>=0:
        b=n.find(a,b)
        if b>=0:
            count+=1
            b+=1        
    return count

print(find(n,a))
