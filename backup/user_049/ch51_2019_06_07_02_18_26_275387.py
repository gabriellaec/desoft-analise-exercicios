def estritamente_crescente(lista):
    numeros=[]
    for i in range(len(lista)):
        if lista[i]>numeros[i]:
            numeros.append(lista[i])
    return lista