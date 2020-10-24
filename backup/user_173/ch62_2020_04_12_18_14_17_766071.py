def pos_arroba (email):
    i = 0
    a = 0
    while i < len(email):
        if email[i][a] == '@':
            return email[i]
        