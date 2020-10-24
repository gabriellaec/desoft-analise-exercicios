def pos_arroba(string):
    i = 0
    for e in string:
        if e == "@":
            return i
        i+=1