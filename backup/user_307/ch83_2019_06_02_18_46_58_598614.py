def  medias_por_inicial(dicio):
    dicio1={}
    
    for nome, med in dicio.items():
        dicio1[nome[0]] = med
        
    for nome, med in dicio1.items():
        x = 0
        i=0
        for name, media in dicio.items():
            if nome[0] == name[0]:
                x += media
                i+=1
        dicio1[nome[0]] = x/i
                
    return dicio1