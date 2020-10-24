def junta_listas(lista):
    i=0
    lista_simples=[]
    while i<len(lista):
        n=0
        while n<len(lista[i]):
            lista_simples.append(lista[i][n])
            n+=1
        i+=1
    return lista_simples