def classifica_lista (x):
    a = len(x)
    i = 0
    while i < a:
        if x == sorted(x[i], key=int) and len(x) > 1:
            return 'crescente'
        elif x == sorted(x[i], key=int, reverse = True) and len(x) > 1:
            return 'decrescente'
        else:
            return 'nenhum'
    