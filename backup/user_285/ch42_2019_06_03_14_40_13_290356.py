def quantos_uns(n):
    ocorrencias=0
    N=str(n)
    for i in N:
        k=str(i)
        if k=='1':
            ocorrencias+=1    
    return ocorrencias