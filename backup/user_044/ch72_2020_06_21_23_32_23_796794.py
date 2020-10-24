def lista_caracteres(string):
    ls = []
    while i<len(string)-1:
        if string[i] not in ls:
            ls.append(i)
    return ls