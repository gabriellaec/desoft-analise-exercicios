def esconde_senha(senha):
    i= 0
    while i < senha:
        barra= '*' * senha[i]
        i += 1
    return barra