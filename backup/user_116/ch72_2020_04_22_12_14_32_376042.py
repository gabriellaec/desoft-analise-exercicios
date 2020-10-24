def lista_caracteres(x):
    lista=[]
    for el in x:
        if el not in lista:
            lista.append(el)
    return lista