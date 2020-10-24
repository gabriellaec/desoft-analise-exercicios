def separa_trios(x):
    i = 0
    lista = []
    while i < len(x):        
        t = x[i:i+3]
        lista.append(t)
        i += 3
                   
    return lista
