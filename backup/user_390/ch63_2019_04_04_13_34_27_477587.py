def pos_arroba(email):
    i=0
    while i<len(email):
        if i=='@':
            return i
        else:
            i+=1