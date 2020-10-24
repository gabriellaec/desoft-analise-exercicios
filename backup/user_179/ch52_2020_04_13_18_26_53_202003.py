def calcula_total_da_nota (l1,l2):
    total = 0
    i = 0
    while i < len(l1):
        total = total + (l1[i] * l2[i])
        i = i + 1
    return total