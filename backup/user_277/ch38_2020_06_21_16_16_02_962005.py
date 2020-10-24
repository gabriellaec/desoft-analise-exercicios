def quantos_uns(n):
    lista = []
    k = str(n)
    for i in k:
        if i == '1':
            r = int(i)
            lista.append(r)
    return len(lista)