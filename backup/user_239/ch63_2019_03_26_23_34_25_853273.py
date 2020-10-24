def pos_arroba(x):
    i=0
    while i<len(x):
        if x[i]=='@':
            a=i
        i+=1
    return a