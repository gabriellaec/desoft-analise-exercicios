def lista_sufixos(stri):
    i=0
    lista=[]
    while i < len(stri):
        S=stri[i:]
        lista.append(S)
        i+=1
    return lista