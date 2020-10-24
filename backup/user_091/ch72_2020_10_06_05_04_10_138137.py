def lista_caracteres(string):
    lista=[]
    i=0
    while i<len(string):
        lista.append(string[i])
        i+=1
    for x in lista:
        i=0
        if x==lista[i]:
            del lista[i]
            i+=1
    return lista