def numero_no_indice (liste):
    listr=[]
    o=0
    for e in liste:
        if e==o:
            listr.append(e)
        o+=1
    return listr

