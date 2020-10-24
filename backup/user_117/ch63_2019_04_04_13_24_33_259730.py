def pos_arroba(email):
    i=0
    on=True
    while i<len(email):
        if email[i]=='@':
            on= False
        i+=1    
        return i

    
    