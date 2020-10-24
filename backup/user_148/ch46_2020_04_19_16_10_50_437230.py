def numero_no_indice(l):
    l2 = []
    i = 0
    
    while i<len(l):
        if l[i] == i:
            l2.append(l[i])
        i += 1
    
    return l2
        