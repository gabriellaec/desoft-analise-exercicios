def subtracao_de_listas(lista1,lista2):
    l3=[]
    i=0
    while i < len(lista1):
        if lista1[i] not in lista2:
            l3.extend(lista1[i])
            i+=1
    return l3
    