def estritamente_crescente(lista_numeros):
    lista_crescente = []
    indice = 0
    for numero in lista_numeros:
        if indice > 0:
            if numero > lista_numeros[indice-1]:
                if numero not in lista_crescente and lista_numeros[indice-1] not in lista_crescente:
                    lista_crescente.append(numero)
                    lista_crescente.append(lista_numeros[indice-1])
        indice += 1
    return lista_crescente