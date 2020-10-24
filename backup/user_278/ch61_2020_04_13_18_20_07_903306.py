def filtra_positivos (l1):
    l2 = []
    for i in range(l1):
        if l1[i] >= 0:
            l2.append(l1[i])
    return l2