def calcula_total_da_nota(lista1, lista2):
    soma=int[]
    if lista1==[] or lista2==[]:
        return 0
    for i in range(len(lista1)):
        for i in range(len(lista2)):
            soma=lista1[i]*lista2[i]
    total_nota=sum(soma)
    return total_nota
        
        