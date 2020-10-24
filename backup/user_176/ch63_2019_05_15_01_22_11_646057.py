def pos_arroba(email):
    i=0
    while counter<len(email):
        if email[i] == '@':
            return i
        counter+=1