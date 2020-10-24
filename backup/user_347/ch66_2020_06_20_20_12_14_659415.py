def lista_sufixos(string):
    lista = []
    for a in string:
        b = string[::(len(string)-a)]
        lista.append(b)
    return b
    