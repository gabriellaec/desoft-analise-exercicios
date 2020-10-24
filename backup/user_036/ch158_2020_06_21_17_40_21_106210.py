with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    res = conteudo.split()
print(len(res))