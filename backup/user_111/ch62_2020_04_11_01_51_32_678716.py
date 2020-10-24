def pos_arroba(email):
    i=0
    x=0
    while i<len(email):
        if email[i]=="@":
            x=i
        i+=1
    return x