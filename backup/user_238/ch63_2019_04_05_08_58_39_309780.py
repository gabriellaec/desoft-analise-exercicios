def pos_arroba(email):
    i=0
    pos=-1
    while i < len(email):
        if email[i]=='@':
            pos = i
        return pos
        i+=1