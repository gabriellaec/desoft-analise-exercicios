def lista_caracteres (string):
    lista = []
    for l in string:
        if l not in lista:
            lista.append(l)
    return lista