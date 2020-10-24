def estritamente_crescente(lista_numeros):
    lista_crescente = []
    maior = lista_numeros[0]
    lista_crescente.append(maior)
    i = 0
    while i < len (lista_numeros):
        if(lista_numeros[i]>maior):
            lista_crescente.append(lista_numeros[i])
            maior = lista_numeros[i]
        i = i + 1

    return lista_crescente