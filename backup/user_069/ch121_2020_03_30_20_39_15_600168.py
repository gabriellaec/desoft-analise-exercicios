def subtracao_de_listas (l1,l2):
    l3 = []
    counter_l1 = 0
    while counter_l1 < len(l1):
        counter_l2 = 0
        aparece = False
        while counter_l2 < len(l2):
            if l1[counter_l1] == l2[counter_l2]:
                aparece = True
        if aparece == False:
            l3.append(l1[counter_l1])
        i += 1
    return l3