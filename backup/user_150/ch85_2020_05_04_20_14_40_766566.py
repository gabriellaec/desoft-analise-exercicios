with open('macacos-me-mordam.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.read()

contador = 0
if leitura == 'Banana' or leitura == 'banana' or leitura == 'BaNaNa' or leitura == 'BANANA':
    contador += 1