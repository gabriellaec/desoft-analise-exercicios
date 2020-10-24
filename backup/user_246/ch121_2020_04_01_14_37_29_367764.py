def subtracao_de_listas(l1,l2):
    x=len(l2)
    i=0
    while i!=x:
        if l1[i] in l2:
            del l1[i]
        i+=1
    return l1
    