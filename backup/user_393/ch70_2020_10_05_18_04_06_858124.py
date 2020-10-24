def esconde_senha(str):
    senha_escondida= []
    i= 0
    while i < len(str):
        senha_escondida.append('*')
        i= i + 1
    return senha_escondida