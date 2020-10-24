def lista_caracteres(palavra):
    lista=[]
    for l in range(len(palavra)):
        if palavra[l] not in lista:
            lista.append(palavra[l])
    return lista