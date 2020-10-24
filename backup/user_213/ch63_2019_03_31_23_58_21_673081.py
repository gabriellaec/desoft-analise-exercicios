def pos_arroba(email):
    i=0
    p=email[i]
    while p!='@':
        i+=1
    return i+1