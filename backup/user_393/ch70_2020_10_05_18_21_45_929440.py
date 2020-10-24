def esconde_senha(str):
    lista_asteriscos= []
    senha_escondida= ''
    i= 0
    while i < len(str):
        lista_asteriscos.append('*')
        senha_escondida= senha_escondida + lista_asteriscos[i]
        i= i + 1
    return senha_escondida
