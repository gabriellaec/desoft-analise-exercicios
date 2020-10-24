def esconde_senha(senha):
    for e in senha:
        escondida = senha.replace(e, '*')
    return escondida