with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    contagem = conteudo.split()

print(contagem)    