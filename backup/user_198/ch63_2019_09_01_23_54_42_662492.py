def pos_arroba(email):
    T=len(email)
    for i in range(0,T):
        if email[i]=="@":
            pos=i
    return(pos)