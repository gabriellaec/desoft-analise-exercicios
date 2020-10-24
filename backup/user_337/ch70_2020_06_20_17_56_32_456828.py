def esconde_senha(senha):
    for i in range(senha):
        senha[i] = '*'
    return senha