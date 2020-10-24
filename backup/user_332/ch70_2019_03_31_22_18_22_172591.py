def esconde_senha(palavra):
    letras = 0
    for e in palavra:
        letras += 1
    senha = "*" * letras
    return senha