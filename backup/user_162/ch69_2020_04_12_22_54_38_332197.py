def junta_listas(l):
    lj = []
    i = 0
    while i < len(l):
        for j in l[i]:
            lj.append(j)
        i+=1
    return lj