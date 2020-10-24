def lista_caracteres(string):
    lista = []
    letra = ''
    for l in string:
        if l != letra:
            letra = l
            lista.append(letra)
    return lista