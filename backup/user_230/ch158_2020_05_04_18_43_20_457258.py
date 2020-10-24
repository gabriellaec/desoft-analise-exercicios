def conta_palavras(texto):
    with open (texto.txt, "r") as arq:
        conteudo=arq.read()
        palavras=conteudo.split()
        return len(palavras)
    