with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    for palavras in conteudo:
        conta_palavras += 1

print(conta_palavras)