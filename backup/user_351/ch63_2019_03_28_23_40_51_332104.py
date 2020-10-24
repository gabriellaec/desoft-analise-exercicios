def pos_arroba(email):
    email=[]
    i = 0
    while i < len(email):
        if email[i] == "@":
            return email[i]
        i +=1