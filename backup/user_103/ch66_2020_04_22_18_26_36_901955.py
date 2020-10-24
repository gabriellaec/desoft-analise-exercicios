def lista_sufixos(string):
    i=0
    lista=[]
    for i in range(len(string)):
        if string not in lista:
            lista.append(string)
        else:
            string-=string[i]
            i+=1
    return lista
