def esconde_senha(string):
    escondida= ''
    for i in range(len(string)):
        escondida= i*'*'
    return escondida
    