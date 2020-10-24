with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
x = conteudo.lower()
y = x.count("banana")
print (y)
