def lista_caracteres (n):
    lista = []
    for i in n:
        if i not in lista:
            lista.append (i)
    return lista