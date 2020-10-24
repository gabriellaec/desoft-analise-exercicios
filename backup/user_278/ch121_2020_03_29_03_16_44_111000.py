def subtraçao_de_listas(lista1,lista2):
    listaUNO=lista1
    listaDOS=lista2
    lista3=[0]
    i=0
    n=0
    while i<len(lista1):
        if listaDOS[n]==listaUNO[i]:
            lista3.append(lista2[n])
            i+=1
        n+=1
    return lista3