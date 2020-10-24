with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    contador = 0
    for palavra in palavras:
        if palavra.lower() == "banana" or palavra.lower() == "banana.":
            contador += 1
print(contador)
