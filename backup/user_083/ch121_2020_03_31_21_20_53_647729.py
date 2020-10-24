def subtracao_de_listas(lista1, lista2):
    listafinal=[0]
    i=0
    for i in range (len(lista1)):
        if lista1[i] not in lista2[i]:
            listafinal.append(lista1[i])
            i+=1
        else:
            i+=1
            continue
        return listafinal
        