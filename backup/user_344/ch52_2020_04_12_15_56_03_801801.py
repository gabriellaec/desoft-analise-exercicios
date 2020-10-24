def calcula_total_da_nota_fiscal(l1,l2):
    i = 0 
    total= 0 
    while i< len(l1):
        total += l1[i]*l2[i]
        i+=1
    return total
    