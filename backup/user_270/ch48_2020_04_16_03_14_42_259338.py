def eh_crescente(l):
    t=False
    for i in range(len(l)-1):
        if l[i]>l[i+1] :
            K = False
            break
        else:
            K = True
    return k