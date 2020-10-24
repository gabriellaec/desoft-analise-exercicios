def lista_sufixos(string):
    stg = str(string)
    i = 0
    lista =[]
    while i < len(stg):
        lista.append(stg[i:])
        i += 1
    return lista
        