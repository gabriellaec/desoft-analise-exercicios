def lista_caracteres(x):
    lista = [x[0]]
    i = 0
    y = 1
    while i+y < len(x):
        if x[i+y] == x[i]:
            y+=1
        else:
            lista.append(x[i])
        i+=1
    print (lista)
    return lista