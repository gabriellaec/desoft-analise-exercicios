def pos_arroba(email):
    i = 0
    for e in email:
        if e != "@":
            i += 1
    return(i)