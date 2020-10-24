def pos_arroba(email):
    string = str(email)
    i = 0
    while i < len(string):
        if string[i] == "@":
            posicao == i
        i += 1
    return posicao
    