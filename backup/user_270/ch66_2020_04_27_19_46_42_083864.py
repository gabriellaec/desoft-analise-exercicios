def lista_sufixos(s):
    lista = []
    i=0
    while i < len(s):
        lista.append(s[i:])
        i+=1
    return lista