def junta_nome_sobrenome (x,y):
    i = 0
    while i < len(x) and (y):
        lista = [x[i], " ", y[i]]
        i += 1
    return lista