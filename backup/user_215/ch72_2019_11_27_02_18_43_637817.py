def lista_caracteres(string):
    lista = []
    for i in range(len(string)):
        if i not in lista:
            lista.append(i)
        i += 1
    return lista