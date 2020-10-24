def pos_arroba(email):
    for i in range(len(email)):
        if i == "@":
            return len(i)
       