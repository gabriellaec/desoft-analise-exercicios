def lista_sufixos(string):
    lista=[]
    i=0
    while i<len(string)-1:
        lista.append(string[i:-1])
        i+=1
    return lista