def classifica_lista (x):
    a = len(x)
    i = 0
    while i < a:
        if x == sorted(x[i], key=int):
            return 'crescente'
        elif x == sorted(x[i], key=int, reverse = True):
            return 'decrescente'
        else:
            return 'nenhum'