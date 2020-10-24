def pos_arroba(email):
    k = 0
    for i in email:
        if i == '@':
            break
        k+=1
    return k