def conta_palavras(x):
    with open(x, "r") as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
    return(len(palavras))