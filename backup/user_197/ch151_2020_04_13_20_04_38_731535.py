def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    if lista==sorted(lista):
        return 'crescente'
    else:
        return 'decrescente'