def junta_nome_sobrenome(a,b):
    i = 0
    lista = []
    while i<len(a) and i<len(b):
        lista[i] = a[i] + b[i]
        i += 1
    return lista