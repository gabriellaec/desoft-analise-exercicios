def esconde_senha(senha):
    for i in senha:
        senha = senha.replace(i,'*')
    return senha