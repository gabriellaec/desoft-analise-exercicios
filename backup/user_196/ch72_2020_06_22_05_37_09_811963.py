def lista_caracteres(string):
    j = []
    for i in string:
        if i not in j:
            j.append(i)
    return j