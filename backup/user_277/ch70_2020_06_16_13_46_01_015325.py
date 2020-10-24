def esconde_senha(string):
    i = 0
    k = ''
    while i < len(string):
        k = k + '*'
        i+=1
    return k
