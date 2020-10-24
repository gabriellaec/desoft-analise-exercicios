def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    for i in lista:
        if lista[i] > lista[i+1]:
            return 'decrescente'
        if lista[i] < lista[i+1]:
            return 'crescente'
        else: 
            return 'nenhum'