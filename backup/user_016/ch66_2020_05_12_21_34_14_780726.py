def lista_sufixos(a):
    lista = []
    lista.append(a)
    i = 1
    while i < len(a):
        b = a.replace(a[len(a)-i],'')
        lista.append(b)
    return lista