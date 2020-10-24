lista=[]
a=input('Palavra: ')
lista.append(a)
while a!='fim':
    lista.append(a)
    a=input('Palavra: ')
i=0
while i<len(lista):
    if len(lista[i])>1 and lista[i][0]=='a':
        print(lista[i])
    i+=1
    
    