def lista_sufixos(palavra):
    lista=[]
    i=0
    while i<len(palavra):
        lista.append(palavra)
        del palavra[i]
        i+=1
    return lista