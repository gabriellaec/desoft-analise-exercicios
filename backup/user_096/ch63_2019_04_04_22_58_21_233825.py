def pos_arroba(email):
    i=0
    while True:
        if email[i] != '@':
            i += 1
        elif email[i] == '@':
            return i 
            break