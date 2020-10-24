def lista_sufixos(string):
    lista_suf = []
    for i in range(0,len(string)):
        lista_suf.append(string[i:])
    return lista_suf
        