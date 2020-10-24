def esconde_senha(senha):
    senha_escondida = []
    i = 0
    while (i < len(senha)):
        senha_escondida.append("*")
        i = i + 1
    senha_escondida = "".join(senha_escondida)
    return senha_escondida