def numero_no_indice (lista):
    numeros=[]
    for i in range(0, len(lista)):
        if i==lista[i]:
            numeros.append(i)
    return (numeros)