def conta_palavras(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return len(palavras)
print(conta_palavras("texto.txt"))
    