def lista_caracteres(string):
    l= []
    for i in string:
        if i not in l:
            l.append(i)
    return l
        