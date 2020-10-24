lista=[]
a=input('Palavra: ')
lista.append(a)
while a!='Fim':
    lista.append(a)
    a=input('Palavra: ')
i=0
while i<len(lista):
    if lista[i][0]=='a':
        print(lista[i])
    i+=1
    
    