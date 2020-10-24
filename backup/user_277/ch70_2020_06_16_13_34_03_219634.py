def esconde_senha(string):
    i = 1
    k = '*'
    while i < len(string):
        k = k + '*'
        i+=1
    return k