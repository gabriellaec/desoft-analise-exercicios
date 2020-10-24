lista=[]
x=0
lista.append(input('palavra: '))
while lista[x]!='fim':
    x+=1
    lista.append(input('palavra: '))
n=len(lista)
i=0
while i<n:
    if lista [i] [0]=='a':
        print (lista[i])
        i+=1
    else:
        i+=1