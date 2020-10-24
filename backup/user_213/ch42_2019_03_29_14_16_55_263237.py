def quantos_uns(num):
    texto=str(num)
    i=0
    uns=0
    while i<len(texto):
        if texto[i]=='1':
            uns+=1
        i+=1
    return uns
        
        