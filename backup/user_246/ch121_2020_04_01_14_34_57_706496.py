def subtracao_de_listas(l1,l2):
    x=len(l2)
    i=0
    while i!=x:
        if l2[i] in l1:
            del l1[i]
        i+=1
    return l1
    