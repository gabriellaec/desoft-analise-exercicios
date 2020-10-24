def esconde_senha(senha):
    for e in senha:
        senha.replace(e, '*')
    return senha