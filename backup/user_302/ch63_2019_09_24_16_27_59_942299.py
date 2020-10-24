def pos_arroba(string):
    i = 0
    posicao = 0
    while i < len(string):
        if string[i] == "@":
            i = posicao
        i += 1
    return posicao