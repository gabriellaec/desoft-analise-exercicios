def lista_caracteres(string):
    lista_de_caracteres = []
    for i in string:
        if i in string:
            lista_de_caracteres.append(i)
        if i in lista_de_caracteres:
            continue
    return lista_de_caracteres
            
            