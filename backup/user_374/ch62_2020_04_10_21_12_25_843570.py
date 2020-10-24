def pos_arroba(email):
    email2 = str(email)
    posicao = 1
    for i in email2:
        if i == '@':
            return posicao
        posicao += 1