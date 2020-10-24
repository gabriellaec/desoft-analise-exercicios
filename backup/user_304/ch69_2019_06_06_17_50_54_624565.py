def junta_listas(lista):
    junta=[]
    i=0
    while i<len(lista):
        j=0
        while j<len(lista[i]):
            junta.append(lista[i][j])
            j+=1
        i+=1
    return junta