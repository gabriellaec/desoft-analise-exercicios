def pos_arroba(str):
    i= 0
    while i < len(str):
        if str[i]== '@':
            break
        i= i + 1
    return i