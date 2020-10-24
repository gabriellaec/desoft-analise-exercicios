def conta_palavra(texto):
    with open("texto.txt", r) as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return len(palavras)