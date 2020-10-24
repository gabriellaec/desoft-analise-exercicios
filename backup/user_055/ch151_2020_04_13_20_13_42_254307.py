def classifica_lista(lista_numeros):
    if len(lista_numeros) < 2:
        return 'nenhum'
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i] > lista_numeros[i + 1] and lista_numeros[i] > lista_numeros[i + 1]:
            return 'nenhum'
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i] > lista_numeros[i + 1]:
            return 'decrescente'
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i] < lista_numeros[i + 1]:
            return 'crescente'