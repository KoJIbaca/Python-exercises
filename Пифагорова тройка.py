#Блок проверки на "дурака"
while True:
    n=input('Введите до какого числа искать:\n')
    try:
        n=int(n)
    except:
        print('Нельзя вводить выражения или буквы\n')
    else:
        break
        
#Поиск чисел        
for c in range (1,n+1, 1):
    for a in range (1,c):
        for b in range (1,a):
            if c**0.5 == (a**2+b**2)**0.5:
                print (a,b,c)
