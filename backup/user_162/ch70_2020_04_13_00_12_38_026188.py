def esconde_senha(senha):
    codigo = ""
    for i in senha:
        i = "*"
        codigo+=i
    return codigo