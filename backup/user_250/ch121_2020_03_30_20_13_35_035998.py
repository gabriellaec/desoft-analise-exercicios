def subtracao_de_listas(l1,l2):
    l3=[]
    i1=0
    while i1 < len(l1):
        if l1[i1] not in l2:
            l3.append(l1[i1])
        i1 += 1
    return l3