def lista_sufixos(string):
    lista=[]
    i=0
    while i < len(string):
        lista.append(string[i:len(string)])

        i+=1

    return lista