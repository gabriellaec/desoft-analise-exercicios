def pos_arroba(email):
    i=0
    tam_email=len(email)
    
    while i < tam_email:
        if email[i] == '@':
            return i
        i+=1