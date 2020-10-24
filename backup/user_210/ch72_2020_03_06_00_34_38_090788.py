for lista_caracteres(s):
    lista = []
    for c in s:
        if c not in lista:
            lista.append(c)
    return lista