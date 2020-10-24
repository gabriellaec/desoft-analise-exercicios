def calcula_total_de_nota (l1,l2):
    # l1 é preços dos produtos
    # l2 é a quantidade compradas

    l3 = []
    for i in (len(l2)):
        p = l1[i]*l2[i]
        l3.append(p)
        
    return l3