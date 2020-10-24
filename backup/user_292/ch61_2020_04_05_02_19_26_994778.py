def filtra_positivos(l):
    lista = []
    a = len(l)
    x = 0
    while x<a:
        if l[x]>=0:
            lista.append(l[x])
            x+=1
        else:
            x+=1
    return lista