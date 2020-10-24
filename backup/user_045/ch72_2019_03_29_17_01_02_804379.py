def lista_caracteres(n):
    i=0
    b=[]
    while i<len(n):
        
        if n[i] not in b:
            b.append(n[i])
        i+=1  
    return b