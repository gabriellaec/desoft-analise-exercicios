def lista_caracteres(string):
    lista = []
    for i in string:
        if string[i+1] != string[i]:
            lista.append(string[i])
    return lista