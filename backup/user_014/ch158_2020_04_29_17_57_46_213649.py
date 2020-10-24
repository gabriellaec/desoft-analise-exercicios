with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    conta_palavras = len(palavras)

print(conta_palavras)