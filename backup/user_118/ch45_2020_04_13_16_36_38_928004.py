lista=[]
numeros=input('Digite números inteiros positivos e armazene-os')
i=0
while numeros>0:
    lista.append(numeros)
    numeros=input('Digite números inteiros positivos e armazene-os')
    i+=1
print (lista[::-1])