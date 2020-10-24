def conta_a (string):
    contagem = {}
    for n in string:
        if n == 'a':
            contagem[n] += 1
        else:
            contagem[n] = 0
    return contagem