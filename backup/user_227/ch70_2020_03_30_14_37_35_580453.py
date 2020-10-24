def esconde_senha(senha):
    return "".join(["*"]*len(senha))

print(esconde_senha("Revolution1"))