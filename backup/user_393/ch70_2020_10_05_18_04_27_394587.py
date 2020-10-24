def esconde_senha(senha):
    senha_escondida= []
    i= 0
    while i < len(senha):
        senha_escondida.append('*')
        i= i + 1
    return senha_escondida