def conta_palavras(texto):
    with open(texto, "r") as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
    return len(palavras)
print(conta_palavras(texto.txt))