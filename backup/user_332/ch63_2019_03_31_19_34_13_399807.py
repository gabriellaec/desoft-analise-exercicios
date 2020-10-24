def pos_arroba(email):
    i = 0
    for e in email:
        if e == "@":
            return (i)
        else:    
            i += 1
    return(i)