def esconde_senha(str):
    senha_escondida= []
    i= 0
    while i < len(str):
        senha_escondida.append('*')
        i= i + 1
    x= 0
    senha_asteriscos= '*'
    while x < len(senha_escondida)-1:
        senha_asteriscos= senha_asteriscos + '*'
        x= x + 1
    return senha_asteriscos
