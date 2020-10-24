def encontra_maximo(l):
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    noval = []
    i = 0
    while i<3:
        noval.append(l1[i])
        noval.append(l2[i])
        noval.append(l3[i])
        i+=1
    return max(noval)