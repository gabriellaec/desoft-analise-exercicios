def calcula_total_da_nota(lista1,lista2):
    a=0
    for i in range(len(lista1)):
        a+=lista1[i]*lista2[i]
    return a