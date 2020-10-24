def calcula_total_da_nota(l1, l2):
    total = 0 
    for i in len(l1):
        total += l1[i]*l2[i]
    return total