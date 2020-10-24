def lista_caracteres(x):
    lista = []
    i = 0
    y = 1
    while i+y < len(x)+1:
        if x[i+y] == x[i]:
            y+=1
        else:
            lista.append(x[i])
        i+=1
    return lista