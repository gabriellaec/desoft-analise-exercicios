def junta_nome_sobrenome(x, y):
    lista = []
    i = 0
    while i < len(x) and i < len(y):
        lista.append(x[i] + y[i])
    return lista