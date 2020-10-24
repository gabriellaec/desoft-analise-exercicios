def lista_caracteres(s):
    lista = []
    for i in s :
        if not i in s :
            lista.append(i)
    return lista