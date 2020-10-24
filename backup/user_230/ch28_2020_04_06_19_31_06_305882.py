lista=[]
lista[0]=1
x=1
while len(lista)==100:
    lista.append(1/2**x)
    x+=1
print (lista)
