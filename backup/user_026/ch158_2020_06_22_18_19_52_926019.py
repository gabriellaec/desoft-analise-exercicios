with open('texto.txt', 'r') as arquivo:
    conteudo= arquivo.read()
    resultado= conteudo.split()
print(len(resultado))