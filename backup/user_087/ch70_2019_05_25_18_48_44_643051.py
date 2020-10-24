def esconde_senha(nome):
    for letra in nome:
        letra = '*'
    return letra*len(nome)
