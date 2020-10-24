def lista_caracteres(string):
    lista=[]
    for i in string:
        if string[i] not in lista:
            string[i].append(lista)
    return lista
            