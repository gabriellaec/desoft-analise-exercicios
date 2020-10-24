def esconde_senha(float(senha)):
    i = 0
    while i < len(senha):
        senha[i] = "*" 
        i += 1
    return senha