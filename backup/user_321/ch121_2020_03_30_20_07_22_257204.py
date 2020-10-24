def subtracao_de_listas(l1,l2):
    lf = []
    i = 0
    while i in range(len(l1)):
        if l1[i] not in l2:
            lf.append(l1[i])
            i += 1
        else:
            i += 1
            continue
    return lf