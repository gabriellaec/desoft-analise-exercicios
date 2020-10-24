def subtracao_de_listas(lista1,lista2):
    i = 0
    if (len(lista1))>0 and (len(lista2))>0:
        for i in range(len(lista1)):
            if (len(lista1))==0:
                return lista_final
            elif (len(lista2)) == 0:
                return lista1
            elif (len(lista1)==0) and (len(lista2) == 0):
                return lista_final
            elif (len(lista1))>0:
                if lista1[i] not in lista2:
                    lista_final.append(lista1[i])
                    i+=1
                if i==(len(lista1)): 
                    return lista_final
    elif (len(lista1))==0 and (len(lista2))==0:
        return lista_final
            
        