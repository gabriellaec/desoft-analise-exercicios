def junta_listas(lista):
    i=0
    n=0
    listanova=[]
    while i<len(lista):
        n=0
        while n<len(lista[i][n]):
            listanova.append(lista[i][n])
            n+=1
        i+=1
    return listanova