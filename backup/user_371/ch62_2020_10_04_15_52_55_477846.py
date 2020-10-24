def pos_arroba(email):
    i=0
    while (len(email)-1)>i:
        if email[i]=="@":
            return i
            i=len(email)-1
        else:
            i+=1