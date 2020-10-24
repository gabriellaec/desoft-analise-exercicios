def lista_caracteres(str):
    lista = []
    i = 0
    while i<len(str):
        if str.count(str[i]) == 1:
            lista.append(str[i])
        i += 1
    return lista
