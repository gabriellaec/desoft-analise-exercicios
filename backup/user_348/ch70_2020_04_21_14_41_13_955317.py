def esconde_senha (senha):
    asteriscos = []
    i = 0
    while i < len(senha):
        asteriscos.append('*')
        i = i + 1
        return asteriscos