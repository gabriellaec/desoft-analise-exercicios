def lista_caracteres(string):
    ls = []
    for i in string:
        if i not in ls:
            ls.append(i)
    return ls