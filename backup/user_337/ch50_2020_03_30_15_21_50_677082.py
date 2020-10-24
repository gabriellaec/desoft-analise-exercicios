def junta_nome_sobrenome(a,b):
    lista = []
    i=0
    while len(lista) <= len(a)+len(b):
        lista.append(a[i])
        lista.append(b[i])
        i += 1
    return lista