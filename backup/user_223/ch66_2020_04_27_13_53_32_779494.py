def lista_sufixos(s):
    lista_substrings=[s]
    i=1
    while i < len(s):
        lista_substrings.append(s[i:])
        i+=1
    return lista_substrings