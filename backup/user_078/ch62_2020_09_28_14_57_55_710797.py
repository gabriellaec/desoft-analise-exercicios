
def pos_arroba(email):
    posicao = -1
    for letra in email:
        if letra == '@':
            posicao += 1
            break

        else:
            posicao += 1
    return posicao