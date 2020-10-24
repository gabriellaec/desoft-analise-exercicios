def classifica_lista(x):
    if len(x) < 2:
        return ('nenhum')
    elif sorted(x) == x:
        return ('crescente')
    elif sorted(x, reverse=True) == x:
        return ('decrescente')
    else:
        return ('nenhum')