def lista_sufixos(s):
    lista = []
    while i < len(s)-1:
        lista.append(s[i:])
        i+=1
    return lista