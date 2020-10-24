def junta_nome_sobrenome(lista1, lista2):
    lista3=[]*len(lista1)
    i=0
    while i<len(lista1):
        lista3[i]=lista1[i]
        lista3[i]=lista1[i] + lista2[i]
        i+=1
    return lista3