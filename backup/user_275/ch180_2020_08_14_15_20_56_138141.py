def ocorrencias_letras(S):
    U=list(set(S))
    C=[]
    for i in range(len(U)):
        N=S.count(U[i])
        C.append(N)
    D=dict(zip(U,C))
    return D