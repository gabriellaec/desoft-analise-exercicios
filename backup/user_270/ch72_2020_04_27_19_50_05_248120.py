def lista_caracteres(s):
    lista = []
    for i in s :
        if not i in s :
            i.append(lista)
    return lista