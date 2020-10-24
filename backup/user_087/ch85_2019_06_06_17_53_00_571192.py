with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
numero_bananas = 0
minusculas = conteudo.lower()
numero_bananas = minusculas.count('banana')
