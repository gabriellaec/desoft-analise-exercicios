def inverte_lista(l):
    l_inv = []
    c = len(l)
    while c >= 0 :
        l_inv.append(l[c])
        c -= 1
    return l_inv
        