def lista_sufixos(s):
    lista_substrings=[]
    i=0
    while i > len(s):
        lista_substrings.append(s[i:])
        i+=1
    return lista_substrings