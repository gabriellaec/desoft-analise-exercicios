def lista_caracteres(string):

    lista_caracteres = []

    for caracter in string:

        if not caracter in lista_caracteres:
            lista_caracteres.append(caracter)

    return lista_caracteres