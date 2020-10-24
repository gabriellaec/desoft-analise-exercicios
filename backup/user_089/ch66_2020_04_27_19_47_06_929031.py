def lista_sufixos(x):
    lista = []
    i = 0
    while i < len(x):
        y = x
        y = y[i:]
                
        lista.append(y)                
        i += 1
        
    return lista