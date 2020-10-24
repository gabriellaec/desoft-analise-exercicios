with open('macacos-me-mordam', 'r') as arquivo:
    conteudo = arquivo.read()

x = conteudo.count('banana', 'Banana', 'BANANA', 'BaNaNa')
print(x)