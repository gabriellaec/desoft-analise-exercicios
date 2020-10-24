with open("texto.txt") as arquivo:
    conteudo = arquivo.read()
    contagem = 0
    for x in conteudo.split(""):
        contagem += 1