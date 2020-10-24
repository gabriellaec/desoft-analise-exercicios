def numero_no_indice (l):
    lista = []
    a = len(l)
    x = 0
    while x<a:
        if l[x] == x:
            lista.append(l[x])
            x+=1
        else:
            x+=1
    return lista