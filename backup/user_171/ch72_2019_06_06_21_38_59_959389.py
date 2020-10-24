def lista_caracteres(palavra):
    lista=[]
    for l in palavra:
        if palavra[l] not in lista:
            lista.append(palavra[l])
    return lista