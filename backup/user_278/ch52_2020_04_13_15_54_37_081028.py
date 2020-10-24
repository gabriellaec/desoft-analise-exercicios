def calcula_total_da_nota (l1,l2):
    # l1 é preços dos produtos
    # l2 é a quantidade compradas

    total = 0

    for i in range(len(l2)):
        total += l1[i]*l2[i]

    return total