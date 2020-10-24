def pos_arroba (email):
    i = 0
    for i in range(len(email)):
        if email[i] == "@":
            return i