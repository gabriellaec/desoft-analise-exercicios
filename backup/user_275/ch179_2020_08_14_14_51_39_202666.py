def posicoes_minusculas(S):
    P=[]
    L= [char for char in S]
    for i in range(len(L)):
        if L[i].islower() == True:
            P.append(i)
    return P