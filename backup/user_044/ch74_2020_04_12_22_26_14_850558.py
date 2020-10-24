def conta_bigramas(stg):
    dn={}
    l=0
    for n in len(stg):
        ocorrencia=0
        s=stg[n]
        x=s+stg[n+1]
        if x in dn:
            l=0
        else:
            for i in len(stg):
                r=stg[i]
                w=r+stg[i+1]
                if x==w:
                    ocorrencia+=1
            dn[x]=ocorrencia
    return dn    
            
    