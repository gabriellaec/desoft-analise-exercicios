def conta_bigramas(stg):
    dn={}
    l=0
    for n in range(len(stg)-1):
        ocorrencia=0
        x=stg[n]+stg[n+1]
        if x in dn.keys():
            l=0
        else:
            for i in range(len(stg)-1):
                y=stg[i]+stg[i+1]
                if x==y:
                    ocorrencia+=1
            dn[x]=ocorrencia
    return dn    
            
    