def pos_arroba(l):
    i = 0
    li = list(l)
    while i < len(li):
        if li[i] == "@":
            return i
        i += 1