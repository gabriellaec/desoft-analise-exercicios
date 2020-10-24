def lista_caracteres (n):
    lista = []
    for i in n:
        if i not in n:
            lista.append (i)
            return lista