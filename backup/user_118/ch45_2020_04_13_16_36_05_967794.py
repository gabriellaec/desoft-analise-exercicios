lista=[]
i=0
while numeros>0:
    numeros=input('Digite números inteiros positivos e armazene-os')
    lista.append(numeros)
    i+=1
print (lista[::-1])