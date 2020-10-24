def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] == "@":
            posicao = i
            break
        else:
            i += 1
    return posicao
        

       