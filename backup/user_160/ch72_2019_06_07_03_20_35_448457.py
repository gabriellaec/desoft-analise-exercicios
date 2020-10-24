def lista_caracteres (n):
    lista = []
    for i in n:
        if i is not in n:
            lista.append (i)
            return lista