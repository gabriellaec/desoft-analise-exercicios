def lista_sufixos(a):
    lista = []
    lista.append(a)
    i = 1
    while i < len(a):
        b = string.replace(a[len(a)-i],'')
        lista.append(b)
    return lista