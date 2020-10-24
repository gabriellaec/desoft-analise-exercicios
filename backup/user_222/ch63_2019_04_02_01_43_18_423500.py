def pos_arroba(email):
    i=0
    while i<len(email):
        if email[i]=="@":
            return email[i+1]
        i+=1
    