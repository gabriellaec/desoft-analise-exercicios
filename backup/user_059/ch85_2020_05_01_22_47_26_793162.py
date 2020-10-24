with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
x = conteudo.upper()
soma = x.count('BANANA')
print(soma)
