with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    
with open ('macacos-me-mordam.txt', 'w') as arquivo:
    conteudo.write(conteudo.upper())
    print(conteudo.find('BANANA'))