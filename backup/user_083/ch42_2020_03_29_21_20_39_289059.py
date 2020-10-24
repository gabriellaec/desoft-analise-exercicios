a=str(input('me diga uma palavra: '))
i=0
lista=['a']*10
while a!='fim':
    if a[0]=='a':
        print(a)
    lista[i]=a
    i+=1
    a=str(input('me diga uma palavra: '))
