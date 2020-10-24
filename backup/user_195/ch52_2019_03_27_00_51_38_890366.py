def eh_crescente(L):
    i=0
    afirmacao=True
    while i<len(L)-1:
        if L[i+1]<=L[i]:
            afirmacao=False
        i+=1
    return afirmacao
            