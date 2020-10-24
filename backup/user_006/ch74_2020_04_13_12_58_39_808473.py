def conta_bigramas(palavra):
    dicio={}
    i=0
    g=0
    naocontem=True
    
    while i<len(palavra)-1:
        davez=palavra[i]+palavra[i+1]
        count=0
        for e in dicio:
            if e!=davez:
                while g<len(palavra)-1:
                    if davez==palavra[g]+palavra[g+1]:
                        count=count+1
                    g=g+1   
        dicio[davez]=count
        i=i+1