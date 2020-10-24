def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    for i in lista:
        if lista[i+1]<lista[i]:
            return 'decrescente'
        if lista[i+1]>lista[i]:
            return'crescente'