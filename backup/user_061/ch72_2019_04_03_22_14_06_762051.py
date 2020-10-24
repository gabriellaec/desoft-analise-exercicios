def lista_caracteres(palavra):
    lista = []
    i=0
    while i<len(palavra):
        if palavra[i] not in lista:
            lista.append(palavra[i])
        i+=1
    return lista