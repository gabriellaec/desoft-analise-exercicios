def agrupa_por_idade(d1):
    c = list()
    ad = list()
    adl = list()
    ido = list()
    new = dict()
    
    for k,v in d1.items():
        
        
        
        if v <= 11:
            c.append(k)
            
           
        elif v >= 12 and v <= 17:
            ad.append(k)
        
        elif v >= 18 and v <= 59:
            adl.append(k)
        
        else:
            ido.append(k)
            
    new['criança'] = c
    new['adolescente'] = ad
    new['adulto'] = adl
    new['idoso'] = ido    
    return(new)
            