def lista_caracteres(x):
    lista = []
    i = 0
    y = 0 
    while i+y < len(x):
        if x[i+y] == x[i]:
            y+=1
        else:
            lista.append(x[i+y])
        i+=1
    print (lista)
    return lista