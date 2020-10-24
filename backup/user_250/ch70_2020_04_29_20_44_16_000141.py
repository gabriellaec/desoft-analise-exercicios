def esconde_senha(password):
    k = 0
    for i in password:
        k += 1
    return "*"*k