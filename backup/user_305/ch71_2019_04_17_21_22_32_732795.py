def esconde_senha(senha):
    i = 0
    while i<=len(senha):
        if len(senha)== i:
            return '*'*i
        i+=1