def esconde_senha(string):
    i = 1
    k = string[0]
    while i < len(string):
        k = k + string[i]
    return k