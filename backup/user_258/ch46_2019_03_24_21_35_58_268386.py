lista=[]
a=input('Palavra: ')
while a!='fim':
    lista.append(a)
    a=input('Outra palavra: ')
i=0
while i<len(lista):
    if len(lista[i])>1 and lista[i][0]=='a':
        print(lista[i])
    i+=1

    