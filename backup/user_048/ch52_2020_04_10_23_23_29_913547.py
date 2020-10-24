def calcula_total_da_nota(listan,listas):
    listac=[]
    for x in range(len(listan)):
        y=listan[x]*listas[x]
        listac.append(y)
    return sum(listac)