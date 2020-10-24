def pos_arroba(email):
    string = str(email)
    for i in string:
        if i == '@':
            posicao = i
    return posicao
    