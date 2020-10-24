def interseccao_valores(x,y):
    lista =[]
    for i in x:
        for t in y:
            if x[i] == y[t]:
                lista.append(x[i])
    return lista