def subtracao_de_listas(lista1,lista2):
    lista3=[]
    contador=0
    while(contador<len(lista1)):
        if(lista1[contador] not in lista2):
            lista3.append(lista1[contador])
        contador+=1
    return lista3
