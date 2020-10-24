def estritamente_crescente(lista):
    numeros = []
    maximo = 0
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            numeros.append(maximo)
    return numeros