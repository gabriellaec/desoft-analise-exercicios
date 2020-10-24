senha = input('digite sua senha: ')


def esconde_senha(senha):
    n = len(senha)*str('*')
    return n
print(esconde_senha(senha))