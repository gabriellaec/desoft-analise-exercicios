with open('macacos-me-mordam.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.readlines()

contador = 0
for palavras in leitura:
    if palavras == 'Banana' or palavras == 'BANANA' or palavras == 'BaNaNa':
        contador += 1