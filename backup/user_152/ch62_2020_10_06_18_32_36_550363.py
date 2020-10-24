def pos_arroba(email):
    i = 0
    while i<len(email):
        if email[i] == "@":
            pos = i +1
        i+=1
    return pos