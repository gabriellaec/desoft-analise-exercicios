def pos_arroba(email):
    i=0
    n=len(email)
    while  i<n:
        if email[i]=='@':
            pos=i
        i+=1
    return pos