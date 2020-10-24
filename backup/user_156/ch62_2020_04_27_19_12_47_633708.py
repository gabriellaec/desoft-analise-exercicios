def pos_arroba(x):
    
    i=0
    while i < len(x):
        if x[i]=="@":
            return i
        i+=1
    