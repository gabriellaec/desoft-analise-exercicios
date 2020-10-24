def pos_arroba(email):
    i=0
    while i<len(email):
        i+=1
        if email[i]=='@':
            return i 