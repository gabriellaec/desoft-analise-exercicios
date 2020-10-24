def esconde_senha(senha):
    i = 0
    while i < len(senha):
        senha[i] = '*'
        #senha.replace(senha[i], '*')
        i += 1
    return senha