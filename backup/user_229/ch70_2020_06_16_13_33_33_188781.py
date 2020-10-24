def esconde_senha(senha):
    nova = ''
    for i in range(len(senha)):
        nova += '*'
    return nova