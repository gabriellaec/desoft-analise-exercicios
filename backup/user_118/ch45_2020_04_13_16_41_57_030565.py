listanumeros = True
while listanumeros:
    lista=[]
    numeros=int(input('Digite números inteiros positivos e armazene-os'))
    if numeros>0:
        lista.append(numeros)
        return lista
    else:
        listanumeros = False
print (lista[::-1])