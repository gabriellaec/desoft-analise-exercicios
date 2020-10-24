def pos_arroba(string):
    i = 0
    pos = 0
    while i < len(string):
        if string[i] == "@":
            pos = i
        i += 1
    return pos