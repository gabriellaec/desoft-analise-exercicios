a=input('Palavra')
lista=[]
while a!='fim':
    lista.append (a)
    a=input('Palavra:')
la=[]
i=0
while i<len(lista):
    if lista[i][0]=='a':
        la.append(lista[i])
    i+=1
print(la)