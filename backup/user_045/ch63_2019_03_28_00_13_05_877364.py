def pos_arroba(n):
    i=0
    while i<len(n):
        if n[i]=='@':
            return i
        i+=1