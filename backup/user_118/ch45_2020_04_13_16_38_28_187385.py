lista=[]
numeros=input('Digite números inteiros positivos e armazene-os')
i=0
while numeros>0:
    lista.append(numeros)
print (lista[::-1])