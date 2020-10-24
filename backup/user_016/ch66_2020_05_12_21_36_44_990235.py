def lista_sufixos(a):
    lista = []
    i = 0
    while i < len(lista):
        lista.append(a[i:])
    return lista