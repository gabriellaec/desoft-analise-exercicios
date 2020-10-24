def subtracao_de_listas(lista1,lista2):
    novalista=[]
    if len(lista1) != 0 and len(lista2) != 0:
        i=0
        while i < len(lista1):
            if lista1[i] not in lista2:
                novalista.append(lista1[i])
                i+=1
            else:
                i+=1
    elif len(lista1) == 0 or len(lista2) == 0:
        novalista = lista1
    return novalista