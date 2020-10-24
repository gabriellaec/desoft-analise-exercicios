def classifica_lista(Lista):
    if len(Lista) < 2:
        return 'nenhum'
    for i in Lista:
        diferenca = Lista[i] - Lista[i-1]
        if diferenca > 0:
            return 'crecente'
        elif diferenca <0:
            return 'decrecente'
        else:
            return 'nenhum'