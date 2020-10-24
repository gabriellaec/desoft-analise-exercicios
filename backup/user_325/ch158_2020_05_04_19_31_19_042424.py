def conta_palavra("texto.txt"):
    with open("texto.txt", r) as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return len(palavras)