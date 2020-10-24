with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    conteudo.upper()
    print(conteudo.find('BANANA'))