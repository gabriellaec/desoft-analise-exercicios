def junta_nome_sobrenome(x,y):
    i = 0
    l = []
    while i < len(x):
        l.append(x[i]+ " " +y[i])
        i += 1
    return l