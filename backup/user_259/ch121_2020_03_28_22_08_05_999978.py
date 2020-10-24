def subtracao_de_listas(lista1,lista2):
	i1 = 0
    i2 = 0
    lista_final = []
    if len(lista1)==0:
        return lista_final
    elif len(lista2)==0:
        return lista1
    else:
        for i1 in range(len(lista1)):
            if i1 == len(lista1):
                return lista_final
            elif i2 == len(lista2):
                i2 = 0
                i1+=1
            if lista1[i1] == lista2[i2]:
                lista_final.append(lista1[i1])
                i2+=1
        return lista_final
                
        