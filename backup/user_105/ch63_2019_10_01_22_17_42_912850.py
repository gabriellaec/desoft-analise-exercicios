def pos_arroba(email):
    i = 0 
    
    for i in email:
        if i == '@':
            break
        if i!='@':
            i += 1

            
    return i
     
     
        