
def junta_nome_sobrenome (x,y):
    i = 0
    lista = []
    while i < len(x):
        lista.append(x[i], " ", y[i])
        i += 1
    return lista