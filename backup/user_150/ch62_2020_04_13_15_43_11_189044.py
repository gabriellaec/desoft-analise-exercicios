def pos_arroba(email):
    for letra in email:
        if letra == '@':
            posicao = email[letra]
    return posicao