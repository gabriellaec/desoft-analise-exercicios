def pos_arroba(email):
    list_email = list(email)
    for i in email:
        if i == "@":
            posicao = [i]
    return posicao