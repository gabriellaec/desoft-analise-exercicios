def mais_frequente(lista):
    maxi=0
    oco={} 
    i=0
    for e in lista:
        n=0
        for i in lista:
            if e==i:
                n=n+1
        oco[e]=n 

    for a in oco.values():
        if a> maxi:
            maxi=a
    for b in oco:
        if oco[b]==maxi:
            return b
            