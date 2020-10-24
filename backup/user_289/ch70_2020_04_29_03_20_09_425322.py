def esconde_senha(senha):
    senha_ = str(senha)
    for e in senha_:
        e = '*'
        string += e
    return string