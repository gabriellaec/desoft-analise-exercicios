def pos_arroba(email):
    i=0
    while i<len(email):
        if email[i]=="@":
            return len(email[i])
         i+=1
        