def interseccao_chaves(d1, d2):
    l = list(d1.value()) 
    l2 = list(d2.value())
    x = len(l)
    y = len(l2)
    k = []
    if x>y:
        for i in range(x):
            if l[i]  in l2:
                k.append(l[i])
    else:
        for i in range(y):
            if l2[i]  in l:
                k.append(l2[i])
    return k