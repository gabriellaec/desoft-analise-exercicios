z=input("palavra? ")
lista=[]
lista.append(z)
i=0
while lista[i]!='fim':
    if lista[i][0]=='a':
        lista.append(z)
        i+=1
    else:
        del lista[i]
    b=input("palavra? ")    
    lista.append(b)
del lista[i]
print(lista)        
    
        