def quantos_uns(num):
    uns=0
    i=0
    while i<len(num):
        if num[i]=="1":
            uns+=1
            
        i+=1
        
    return uns
