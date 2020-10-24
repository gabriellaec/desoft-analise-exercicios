def lista_sufixos(x):
    lista = []
    i = 0
    while i < len(x):
        lista.append(x)
        i += 1
        x = x[i:]
        
    return lista