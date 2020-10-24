def pos_arroba(s):
    i = 0
    while i < len(s):
        if s[i] == "@":
            break
        else:
            i+=1
    return i
        