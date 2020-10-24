def esconde_senha(senha):
    senha2 = ""
    for letra in senha:
        senha2 += "*"
    return senha2