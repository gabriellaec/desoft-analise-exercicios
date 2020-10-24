def junta_nome_sobrenome(a,b):
    lista = a
    i=1
    t = 0
    while len(lista) <= len(a)+len(b):
        lista.insert(i,b[t])
        i += 2
        t += 1
    return lista