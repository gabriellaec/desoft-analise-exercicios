def esconde_senha(senha):
    senha_escondida= []
    i= 0
    while i < len(senha):
        senha_escondida.append('*')
        i= i + 1
    x= 0
    senha_asteriscos= '*'
    while x < len(senha_escondida):
        senha_asteriscos= senha_asteriscos + '*'
        x= x + 1
    return senha_asteriscos
