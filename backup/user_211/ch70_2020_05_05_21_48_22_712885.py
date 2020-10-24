def esconde_senha(senha):
    senha[::] = "*"
    return senha