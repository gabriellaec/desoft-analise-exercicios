def lista_caracteres(x):
    i=0
    l=[]
    while i < len (x):
        if x[i] not in l:
            l.append(x[i])
        i+=1
    return l
            
            
        