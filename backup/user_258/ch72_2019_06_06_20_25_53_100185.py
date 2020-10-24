def lista_caracteres(string):
    lista = []
    for k in string:
        if k not in lista:
            lista.append(k)
    return lista