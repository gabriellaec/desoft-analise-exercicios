def pos_arroba(email):
    i = 1
    for e in email:
        if e != "@":
            i += 1
    return(i)