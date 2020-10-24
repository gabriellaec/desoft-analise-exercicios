def medias_por_inicial(nomes):
    i={}
    for c,v in nomes.items():
        if c(0) not in i.keys:
            i[c(0)]=[]
        i[c(0)].append(v)
    return i
         
            
            
    