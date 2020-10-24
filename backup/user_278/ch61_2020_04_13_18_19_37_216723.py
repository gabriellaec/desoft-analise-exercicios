def filtra_positivos (l1):
    l2 = []
    i = 0
    for i in range(0,len(l1)):
        if l1[i] >= 0:
            l2.append(l1[i])
            i+=1
        else:
            i+=1
    return l2