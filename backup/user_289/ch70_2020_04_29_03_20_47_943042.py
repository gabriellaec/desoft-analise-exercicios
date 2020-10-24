def esconde_senha(senha):
    senha_ = str(senha)
    for e in senha_:
        e = '*'
        senha_escondida += e
    return senha_escondida