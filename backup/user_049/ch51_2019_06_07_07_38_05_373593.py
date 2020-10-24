def estritamente_crescente(lista):
    numeros=[]
    maximo=0
    for i in lista:
        if lista[i] > maximo:
            maximo = lista[i]
            numeros.append(maximo)
    return numeros