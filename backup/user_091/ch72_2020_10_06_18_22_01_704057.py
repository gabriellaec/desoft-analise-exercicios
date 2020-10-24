def lista_caracteres(string):
    lista=[]
    i=0
    while i<len(string):
        lista.append(string[i])
        i+=1
    p=1
    while p<len(lista)-1:
        g=lista[0]
        if g!=lista[p]:
            g=lista[p]
            p+=1
            
        else:
            del lista[p]
            p+=1
            

    return lista