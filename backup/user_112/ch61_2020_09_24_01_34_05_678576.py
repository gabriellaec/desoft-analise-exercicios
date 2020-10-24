def filtra_positivos(n):
    x = len(n)
    i = 0
    lista = []
    while i < x:
        for item in n:
            if item > 0:
                lista.append(item)
                i = i + 1
            else:
                i = i + 1
    return(lista)