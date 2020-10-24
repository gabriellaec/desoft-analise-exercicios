with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
palavras = texto.split(' ')
i = 0
for palavra in palavras:
    if palavra.upper() == 'BANANA':
        i+=1
print(i)