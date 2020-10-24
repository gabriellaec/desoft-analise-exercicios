def subtracao_de_listas(l1,l2):
    lf = []
    for i in range(len(l1)):
        if l1[i] not in l2:
            lf.append(l1[i])
        else:
            continue
    return lf