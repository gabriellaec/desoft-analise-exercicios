def calcula_total_da_nota(lista1,lista2):
    preco=[]
    while(i<len(lista1)):
        preco.append(lista1[i]*lista2[i])
    return (sum(preco))