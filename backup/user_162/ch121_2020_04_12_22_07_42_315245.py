def subtracao_de_listas(l1, l2):
    for i in l2:
        g = 0
        while g < len(l1):
            if i == l1[g]:
                del l1[g]
            g+=1
    return l1