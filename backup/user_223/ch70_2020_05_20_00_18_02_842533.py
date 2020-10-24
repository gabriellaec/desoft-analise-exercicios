def esconde_senha(senha):
    for e in senha:
        replace(e, '*')
    return senha