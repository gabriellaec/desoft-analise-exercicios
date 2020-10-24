def quantos_uns(n):
    ocorrencias=0
    n=' '
    for i in len(n):
        if n[i]=='1':
            ocorrencias+=1    
    return ocorrencias