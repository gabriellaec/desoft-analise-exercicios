with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()

x = conteudo.count('banana', 'Banana')
y = conteudo.count('BANANA', 'BaNaNa')
print(x+y)