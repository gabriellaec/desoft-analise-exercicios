def lista_caracteres(lista):
    i=0
    quebra=[]
    while i<len(lista):
        if lista[i]!=lista[i-1]:     
            quebra.append(lista[i])
        i+=1
    return(quebra)