def pos_arroba(string):
    i = 0
    posicao = 0
    while i < len(string):
        if string[i] == "@":
            posicao = i
        i += 1
    return posicao