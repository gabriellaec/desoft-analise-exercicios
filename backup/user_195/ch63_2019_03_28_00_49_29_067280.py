def pos_arroba(p):
    r=0
    i=0
    while i<len(p):
        if p[i]=="@":
            r=i
        i+=1
    return r