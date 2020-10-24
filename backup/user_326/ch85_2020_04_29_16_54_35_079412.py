with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
palavras_minusculas = conteudo.lower()
conta_bananas = palavras_minusculas.count('banana')
