with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
palavras_minusculas = conteudo.lower()
print(palavras_minusculas)
conta_bananas = palavras_minusculas.count('banana')
print(conta_bananas)
