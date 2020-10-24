def conta_ocorrencias(a):
    dic={}
    c=0
    for i in lista:
        for a in lista:
            if i==a:
                c+=1
        dic[i]=c
        c=0
    return dic