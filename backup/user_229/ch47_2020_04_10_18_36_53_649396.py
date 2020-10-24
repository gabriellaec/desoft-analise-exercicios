def estritamente_crescente(numeros):
    lista = []
    lista[0] = numeros[0]
    for i in range(numeros):
        if numeros[i+1] > numeros[i]:
            lista.append(numeros[i+1])
    return lista
print(lista)