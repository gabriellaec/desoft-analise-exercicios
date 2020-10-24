a=input('Palavra:')
lista=[]
while a!='fim':
    lista.append (a)
    a=input('Palavra:')
i=0
while i<len(lista):
    if lista[i][0]=='a':
        del lista[i]
    i+=1
print(lista)