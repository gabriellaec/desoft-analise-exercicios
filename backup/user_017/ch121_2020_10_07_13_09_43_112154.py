def subtracao_de_listas(lista_1,lista_2):
   
    i=0
    while i<len(lista_1):
        k=0
        while k<len(lista_2):
            if lista_1[i] == lista_2[k]:
                lista_1.remove(lista_1[i])
            k+=1
        i+=1
    return lista_1