def quantos_uns(n):
    ocorrencias=0
    N=str(n)
    for i in N:
        if N[i]=="1":
            ocorrencias+=1    
    return ocorrencias