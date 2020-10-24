def estritamente_crescente(x):
    lista = []
    y = 0
    while y < len(x):
        if x[y]>x[y-1]:
            lista.append(x[y])
            y+=1
        else:
            y+=1
    return lista