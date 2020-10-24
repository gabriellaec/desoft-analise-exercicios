def estritamente_crescente(numeros):
    lista = [numeros[0]]
    for i in range(numeros-1):
        if numeros[i+1] > numeros[i]:
            lista.append(numeros[i+1])
    return lista