def junta_nome_sobrenome(a,b):
    t = 0
    lista = []
    while t < len (a):
        x = "{0} {1}".format(a[t], b[t])
        lista.append(x)
        t += 1
    return lista