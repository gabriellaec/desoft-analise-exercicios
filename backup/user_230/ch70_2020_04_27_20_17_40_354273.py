def esconde_senha (senha):
    string=senha
    for i in senha:
        string=senha.replace(i,"*")
    return string