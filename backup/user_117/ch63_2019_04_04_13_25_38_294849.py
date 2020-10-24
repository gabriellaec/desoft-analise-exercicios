def pos_arroba(email):
    i=0
    on=True
    while on:
        if email[i]=='@':
            on= False
        i+=1    
        return i

    
    