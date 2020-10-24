def lista_caracteres(asdf):
    lista = []
    for i in range(len(asdf)):
        if asdf[i] not in lista:
            lista.append(asdf[i])
            
    return lista
    
    