lista=[]
a=input('Palavra: ')
while a!='fim':
    lista.append(a)
    a=input('Outra palavra: ')
i=0
while i<len(lista):
    a=lista[i]
    if len(a)==1 and a[0]=='a':
        print(a)
    i+=1

    