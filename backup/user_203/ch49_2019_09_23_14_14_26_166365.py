numeros=int(input('Digite Numeros inteiros: ')) 
lista=[] 
while numeros>0:
    lista.append(numeros)
    numeros=int(input('Digite Numeros inteiros: '))
print(lista[ : : -1]) 
