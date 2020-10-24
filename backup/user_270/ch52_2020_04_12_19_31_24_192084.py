def calcula_total_da_nota(l1,l2):
    i = 0
    p = 0
    while i < len(l1):
        soma = l1[i]*l2[i]
        p += soma
        i += 1
    return soma