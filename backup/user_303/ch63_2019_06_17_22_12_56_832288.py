def pos_arroba(email): 
    s=0
    for w in email:
        s+=1
        if w == "@":
            s-2
            return s 