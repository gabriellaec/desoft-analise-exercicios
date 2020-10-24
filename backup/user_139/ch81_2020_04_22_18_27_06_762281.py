def interseccao_valores (x, y):
    lista = []
    for v in x.values():
        lista.append(v)
    for v in y.values():
        lista.append(v)
    return lista
print (interseccao_valores({'A': 1, 'B': 2, 'C': 3, 'D': 4}, {'A': 5, 'B': 6, 'C': 7, 'E': 8}))
