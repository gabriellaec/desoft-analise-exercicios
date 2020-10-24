def pos_arroba(palavra):
    k=len(palavra)
    for i in range(0,k):
        if palavra[i]=='@':
            r=i+1
            return r