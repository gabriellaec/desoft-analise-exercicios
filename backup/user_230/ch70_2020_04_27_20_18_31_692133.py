def esconde_senha (senha):
    string=senha
    for i in senha:
        string=string.replace(i,"*")
    return string