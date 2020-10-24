def quantos_uns(n):
    ocorrencias=0
    n=' '
    for e in n:
        if n[e]=='1':
            ocorrencias+=1    
    return ocorrencias