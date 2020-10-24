def conta_palavra(texto):
    with open(texto, "r") as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return len(palavras)
print(conta_palavras("texto.txt"))