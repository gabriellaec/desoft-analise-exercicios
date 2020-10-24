def lista_sufixos(string):
    s=string
    lista=[]
    while len(s)>1:
        del(s[0])
        lista.append(s)
    return(lista)