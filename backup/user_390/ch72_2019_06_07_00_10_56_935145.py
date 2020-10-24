def lista_caracteres(string):
    c=0
    lista=[]
    for i in string:
        if i not in lista:
            lista.append(i)
    return lista
        
        