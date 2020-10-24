def esconde_senha(palavra):
    for i in palavra:
        palavra=palavra.replace(i,"*")
    return palavra