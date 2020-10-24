def pos_arroba(string):
    i = 0
    while i <= len(string):
        if string[i] == '@':
            return i
            break