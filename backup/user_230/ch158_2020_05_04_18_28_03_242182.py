def conta_palavras(texto.txt):
    while open (texto.txt, "r") as arq:
        conteudo=arq.read().split()
        return len(conteudo)
    