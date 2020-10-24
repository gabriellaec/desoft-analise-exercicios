def esconde_senha (senha):
    string=senha
    for i in range (0, len(senha)):
        string=senha.replace(i,"*")
    return string