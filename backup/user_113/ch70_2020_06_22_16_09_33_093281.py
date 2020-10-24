def esconde_senha(senha):
    i = 0
    while i < len(senha):
        senha.replace(senha[i], '*')
        i += 1
    return senha