def lista_caracteres(a):
    lista = list()
    for i in a:
        if i not in lista:
            lista.append(i)
            
    return lista