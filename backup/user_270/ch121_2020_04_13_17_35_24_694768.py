def subtracao_de_listas(l1,l2):
    l3 = []
    for i in l1:
        if not i in l2 :
            l3.append(i)
    return l3