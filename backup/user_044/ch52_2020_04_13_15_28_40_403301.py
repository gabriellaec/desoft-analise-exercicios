def calcula_total_da_nota(ls1,ls2):
    total=0
    for i in range(len(ls1)):
        total+=(ls1[i]*ls2[i])
    return total