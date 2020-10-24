def junta_nome_sobrenome(lista1, lista2):
    lista3=[0]*len(lista1)
    i=0
    while i<len(lista1):
        a=str(lista1[i])
        b=str(lista2[i])
        lista3[i]=(a,b)
        i+=1
    return lista3