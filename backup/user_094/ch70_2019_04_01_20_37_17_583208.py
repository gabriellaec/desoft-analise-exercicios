senha = input("qual a sua senha? ")
def esconde_senha(senha):
    senha_hidden = "*" * len(senha)
    return senha_hidden

print (esconde_senha(senha))