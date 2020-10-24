def classifica_lista (Lista):
    if Lista == []:
        return 'nenhum'
    if len(Lista) < 2:
        return 'nenhum'
    for c in Lista:
        if Lista == sorted(Lista, reverse = True):
            return 'decrescente'
        if Lista == sorted(Lista):
            return'crescente'
        else:
            return'nenhum'
        