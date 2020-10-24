def pos_arroba(n):
    i = 0
    while i < len(n):
        if n[i] == '@':
            break
        i += 1
    return i