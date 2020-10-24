def estritamente_crescente(x):
    i = 0
    lista = [x[0]]
    while i < len(x):
        if x[i] > x[0]:
            lista.append(x[i])
        i += 1
    return lista
        
        