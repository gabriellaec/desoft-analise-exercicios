def encontra_maximo (matriz):
    l = []
    for i in matriz: #retorna listas dentro da lista matriz
        for t in i: #retorna os valores das listas da lista matriz
            l.append(abs(t))
    return max(l)