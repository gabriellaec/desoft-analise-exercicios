def estritamente_crescente(numeros):
    if numeros == []:
        return []
    else:
        lista = [numeros[0]]
        for i in range(len(numeros)-1):
            if numeros[i+1] > numeros[i]:
                lista.append(numeros[i+1])
        return lista
print(estritamente_crescente(numeros))