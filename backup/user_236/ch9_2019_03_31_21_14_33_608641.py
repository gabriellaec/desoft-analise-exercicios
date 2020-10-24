def lista_sufixos(string):
    s=string
    lista=[]
    while s[0]==' ':
        del(s[0])
    while len(s)>0:
        lista.append(s)
        del(s[0])
    return(lista)