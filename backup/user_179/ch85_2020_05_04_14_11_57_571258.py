with open('macacos-me-mordam.txt', 'r') as texto:
    conteudo = texto.read()
    conteudo.lower()

x = conteudo.find('banana')
contador = len(x)
print(contador)