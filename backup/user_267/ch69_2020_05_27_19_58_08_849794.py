def junta_listas(a):
    lista=[]
    w = 0
    while w < len(a):
        for i in a:
            lista.append(i[w])
            w += 1
    return lista
   