def estritamente_crescente(numeros):
    lista = []
    for i in range(numeros):
        if numeros[i+1] > numeros[i]:
            lista.append(numeros[i+1])
    return lista