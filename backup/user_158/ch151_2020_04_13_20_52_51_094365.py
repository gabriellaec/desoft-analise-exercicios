def classifica_lista(Lista):
    if len(Lista) < 2:
        return 'nenhum'
    for i in len(Lista):
        diferenca = Lista[i] - Lista[i-1]
        if diferenca > 0:
            return 'crescente'
        elif diferenca <0:
            return 'decrescente'
        else:
            return 'nenhum'