def esconde_senha(senha):
    separa = senha.split()
    for i in separa:
        separa[i] == "*"
    junta = senha.join()
    return junta