def inverte_lista(a):
    y = len(a)
    lista =[]
    while y > 0:
        lista.append(a[y - 1])
        y -= 1
    return lista