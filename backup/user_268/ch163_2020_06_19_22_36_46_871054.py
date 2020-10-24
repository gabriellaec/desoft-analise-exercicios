def calcula_media(lt):
    
    als = []
    nts = 0

    
    for i in lt:
        
        v = i.values()
        k = i.keys()
        
        for r in k:
            als.append(r)
        
        for j in v:
            nts += j
            
    media = nts/(len(als))
    
    return media
            
            