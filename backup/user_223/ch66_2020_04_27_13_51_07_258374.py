def lista_sufixos(s):
    lista_substrings=[]
    i=len(s)
    while i > 0:
        lista_substrings.append(s[i:])
        i-=1
    return lista_substrings