def junta_nome_sobrenome(x, y):
    i = 0
    d = []
    a = x[i] + " " + y[i]
    d.append(a)
    i += 1
    while i < len(lista1):
        a = x[i]+" "+y[i]
        d.append(a)
        i += 1
    return d