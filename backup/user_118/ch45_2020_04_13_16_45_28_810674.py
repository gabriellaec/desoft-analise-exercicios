listanumeros = True
while listanumeros:
    lista=[]
    numeros=int(input('Digite números inteiros positivos e armazene-os'))
    if numeros>0:
        lista.append(numeros)
    else:
        listanumeros = False
        return lista
print (lista[::-1])