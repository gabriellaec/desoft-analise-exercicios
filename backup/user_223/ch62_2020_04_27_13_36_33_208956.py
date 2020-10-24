def pos_arroba(email):
    i=0
    while i < len(email)-1:
        if email[i] == "@":
            posicao = i
        else:
            i+=1
    return posicao