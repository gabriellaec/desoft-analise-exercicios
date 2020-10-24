def pos_arroba(email):
    string = str(email)
    i = 0
    while i <= len(string):
        if i == '@':
            posicao = i
        else:
            i += 1
    return posicao
    