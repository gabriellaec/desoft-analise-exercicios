def junta_nome_sobrenome(a,b):
    t = 0
    lista = []
    x = a[t]+""+b[t]
    while t < len (a):
        lista.append(x)
        t += 1
    return lista