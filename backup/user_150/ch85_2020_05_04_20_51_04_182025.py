with open('macacos-me-mordam.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.read()
    palavras = leitura.split()

contador = 0
for palavra in palavras:
    for i in range(len(palavras)):
        if palavra.lower() == 'banana':
            contador += 1
        elif palavra.lower() == 'banana.':
            contador += 1
print(contador)