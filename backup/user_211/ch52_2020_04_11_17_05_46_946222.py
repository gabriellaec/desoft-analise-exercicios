def calcula_total_da_nota(lista1,lista2):
    preco=[]
    i=0
    while(i<len(lista1)):
        preco.append(lista1[i]*lista2[i])
        i+=1
    return (sum(preco))