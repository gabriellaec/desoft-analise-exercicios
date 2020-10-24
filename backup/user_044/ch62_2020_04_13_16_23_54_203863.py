def pos_arroba(mail):
    for i in range(len(mail)):
        if mail[i] == '@':
            return i
            