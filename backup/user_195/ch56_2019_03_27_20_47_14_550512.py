def calcula_total_da_nota(L,S):
    i=0
    total=0
    while i<len(L):
        item=0
        item=L[i]*S[i]
        total+=item
        i+=1
    return total