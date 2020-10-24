def conta_letras(x):
    ocorrencia=0
    dn={}
    l=0
    for n in x:
        if n in dn:
            l=o
            
        else:
            for i in x:
                if n==i:
                    ocorrencia+=1
            dn[n]=ocorrencia
    return dn