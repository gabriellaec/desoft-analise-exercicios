def conta_palavras(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.readlines()
        palavras = conteudo.split()
        return len(palavras)
