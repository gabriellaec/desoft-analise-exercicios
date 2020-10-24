def lista_sufixos(a):
    x = len(a)
    lista = []
    i = 1
    p = ""
    while i < x:
        p = p + a[i]
        i += 1
        lista.append(p)
    p = ""    
    return lista