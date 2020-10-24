def junta_nome_sobrenome(a,b):
    i = 0
    lista = []
    while i+1<len(a) and i+1<len(b):
        lista[i] = a[i] + b[i]
        i += 1
    return lista