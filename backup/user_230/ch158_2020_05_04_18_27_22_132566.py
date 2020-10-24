def conta_palavras(texto):
    while open ("texto.txt") as arq:
        conteudo=arq.read().split()
        return len(conteudo)
    