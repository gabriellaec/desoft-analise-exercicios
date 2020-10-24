with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.split()
    x = len(a)
print(x)