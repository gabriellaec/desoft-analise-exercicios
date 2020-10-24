
def pos_arroba(email):
    posicao = 0
    for i in email:
        if i != '@':
            posicao += 1
        else:
            posicao += 1
            break
    return posicao