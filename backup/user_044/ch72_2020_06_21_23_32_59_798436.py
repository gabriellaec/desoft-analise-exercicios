def lista_caracteres(string):
    ls = []
    i = 0
    while i<len(string):
        if string[i] not in ls:
            ls.append(i)
        i += 1
    return ls