def classifica_lista(numeros):
    crescente = True
    decrescente = True
    if len(numeros) < 2:
        return 'nenhum'
    i = 1
    while i < len(numeros):
        if numeros[i-1] >= numeros[i]:
            crescente = False
        if numeros[i-1] <= numeros[i]:
            decrescente = False
        i += 1
    if crescente:
        return 'crescente'
    if decrescente:
        return 'decrescente'
    else:
        return 'nenhum'