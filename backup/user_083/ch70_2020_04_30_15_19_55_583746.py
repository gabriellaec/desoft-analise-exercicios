def esconde_senha(senha):
    for i in range(len(senha)):
        r=senha.replace(senha[i],'*')
        return r