def estritamente_crescente(lista_numeros):
    if lista_numeros == []:
        return lista_numeros
    else:
        n_crescente = lista_numeros[0]
        lista_crescente = [n_crescente]
        for i in range(len(lista_numeros) - 1):
            if lista_numeros[i + 1] > n_crescente:
                lista_crescente.append(lista_numeros[i + 1])
                n_crescente = lista_numeros[i + 1]
        return lista_crescente