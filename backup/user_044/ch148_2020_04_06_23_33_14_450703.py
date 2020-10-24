def conta_letras(x):
    ocorrencia=0
    dn={}
    a=0
    for n in x:
        if n in dn:
            a=0
        else:
            for i in x:
                if n==i:
                    ocorrencia+=1
    dn{n}=ocorrencia
    return dn