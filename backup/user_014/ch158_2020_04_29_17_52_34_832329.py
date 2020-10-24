with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    conta_palavras = 0
    for palavras in len(palavras):
        conta_palavras += 1

print(conta_palavras)