def pos_arroba(email):
    counter=0
    while counter<len(email):
        if email[counter] == '@':
            return counter
        counter+=1