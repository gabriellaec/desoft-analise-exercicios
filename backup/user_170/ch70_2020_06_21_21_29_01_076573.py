def esconde_senha(senha):
    hidden = ""
    for i in range(len(senha)):
        hidden += "*"
    return hidden