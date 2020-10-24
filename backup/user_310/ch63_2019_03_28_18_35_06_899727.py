def pos_arroba(l):
    
    i=0
    
    while i<len(l):
        if l[i]=="@":
            return i
        i+=1