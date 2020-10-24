with open ("texto.txt", "r") as arq:
    conteudo=arq.read()
palavras=conteudo.split()
print (len(palavras))
    