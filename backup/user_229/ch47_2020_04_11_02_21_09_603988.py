def estritamente_crescente(numeros):
    if numeros == []:
        return []
    else:
        lista = [numeros[0]]
        maior = numeros[0]
        for i in range(len(numeros)-1):
            if numeros[i+1] > maior:
                lista.append(numeros[i+1])
                maior = numeros[i+1]
        return lista