def classifica_lista(Lista):
    if len(Lista) < 2:
        return 'nenhum'
    if Lista == []:
        return 'nenhum'
    for c in Lista:
        if Lista == sorted(Lista):
            return 'crescente'
        if Lista == sorted(Lista, reverse = True):
            return 'decrescente'
        else:
            return 'nenhum'
            