def monta_dicionario(L,M):
    D={}
    x=0
    for c in L:
        for h in M:
            h=M[x]
            x+=1
            D[c]=h
            break
    return D