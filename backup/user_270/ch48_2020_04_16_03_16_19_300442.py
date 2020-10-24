def eh_crescente(l):
    K=False
    for i in range(len(l)-1):
        if l[i]>=l[i+1] :
            K = False
        else:
            K = True
    return K