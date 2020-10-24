def simplifica_dict(d):
    lista = []
    for i in d:
        if i not in lista:
            lista.append(i)
        if d[i] not in lista:
            lista.append(d[i])
    return(lista)

       
        