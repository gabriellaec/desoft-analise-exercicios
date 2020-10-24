def estritamente_crescente(x):
    lista = []
    número = x[0]
    lista.append(número)
    y = 1
    while y < len(x):
        if x[y]>x[y-1]:
            valor = x[y]
            lista.append(valor)
            y+=1
        else:
            y+=1
    return lista