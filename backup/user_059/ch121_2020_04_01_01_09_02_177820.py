def subtracao_de_listas(l1, l2):
    l=[]
    i = 0
    while i<len(l1):
        if l1[i] not in l2:
            l.append(l1[i])
        i+=1            
    return l