def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] == '@':
            print(i + 1)
            break
        i += 1