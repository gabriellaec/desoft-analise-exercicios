with open('macacos-me-mordam.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.readlines()

contador = 0
for palavras in leitura:
    for i in range(len(palavras)):
        if palavras[i:i+6] == 'Banana' or palavras[i:i+6] == 'BANANA' or palavras[i:i+6] == 'BaNaNa' or palavras[i:i+6] == 'banana':
            contador += 1