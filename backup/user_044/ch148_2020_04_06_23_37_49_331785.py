def conta_letras(x):
    ocorrencia=0
    dn={}
    l=0
    for n in x:
        ocorrencia=0
        if n in dn:
            l=0   
        else:
            for i in x:
                if n==i:
                    ocorrencia+=1
            dn[n]=ocorrencia
    return dn