def esconde_senha(senha):
    i = 0
    while i < len(senha):
        senha.replace(senha[i], "*")
        #senha[i] = float("*") 
        i += 1
    return senha