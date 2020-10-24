def pos_arroba(email):
    i = 0
    pos = - 1
    while i < len(email): 
        if email[i] == "@":
            pos = i 
        i +=1
        
    retun pos