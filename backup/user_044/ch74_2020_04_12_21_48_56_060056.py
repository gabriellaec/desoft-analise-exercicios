def conta_bigramas(stg):
    dc={}
    l=0
    for n in stg:
        ocorrencia=0
        x=n+stg[n+1]
        if x in dn:
            l=0
        else:
            for i in stg:
                y=i+stg[i+1]
                if x==y:
                    ocorrencia+=1
            dn[x]=ocorrencia
    return dn    
            
    